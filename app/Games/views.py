import requests
from datetime import datetime
from django.views.generic import DetailView, ListView
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required
from django.contrib import messages

from .models import Game, UserGameList

User = get_user_model()


# -------------------
# Páginas principais
# -------------------
def home(request):
    games = Game.objects.all()
    return render(request, 'home.html', {'games': games})


def listar_jogos(request):
    jogos = Game.objects.all()
    return render(request, 'listar_jogos.html', {'jogos': jogos})


# -------------------
# Detalhe de jogo
# -------------------
class Games(DetailView):
    model = Game
    template_name = 'games.html'

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        game = self.get_object()
        user = self.request.user

        if user.is_authenticated:
            # Pega o registro do usuário para esse jogo
            ug = UserGameList.objects.filter(user=user, game=game).first()
            ctx['in_list'] = bool(ug)
            ctx['user_status'] = ug.status if ug else 'P'  # padrão Para Jogar
        else:
            ctx['in_list'] = False
            ctx['user_status'] = None

        return ctx


# -------------------
# Integração IGDB
# -------------------
CLIENT_ID = "66vd402qci2oa706lzsxck2myaqput"
CLIENT_SECRET = "drvthppx8c27f7eryv6qo739r2cfpz"


def get_igdb_token():
    url = "https://id.twitch.tv/oauth2/token"
    params = {
        "client_id": CLIENT_ID,
        "client_secret": CLIENT_SECRET,
        "grant_type": "client_credentials"
    }
    resp = requests.post(url, params=params)
    resp.raise_for_status()
    return resp.json()["access_token"]


def preencher_e_salvar(request):
    if request.method == "POST":
        nome_jogo = request.POST.get("nome")
        token = get_igdb_token()
        headers = {
            "Client-ID": CLIENT_ID,
            "Authorization": f"Bearer {token}"
        }
        body = f'''
            search "{nome_jogo}";
            fields name, genres.name, first_release_date, summary, involved_companies.company.name, cover.url, artworks.url, videos.video_id;
            limit 1;
        '''
        resp = requests.post("https://api.igdb.com/v4/games", headers=headers, data=body)
        resp.raise_for_status()
        dados = resp.json()

        if dados:
            jogo = dados[0]

            # Evitar duplicados
            if Game.objects.filter(title__iexact=jogo.get("name", "")).exists():
                return redirect("listar_jogos")

            genero = ""
            if "genres" in jogo and jogo["genres"]:
                try:
                    genero = jogo["genres"][0]["name"]
                except (TypeError, KeyError):
                    genero = ""

            desenvolvedor = ""
            if "involved_companies" in jogo and jogo["involved_companies"]:
                try:
                    desenvolvedor = jogo["involved_companies"][0]["company"]["name"]
                except (TypeError, KeyError):
                    desenvolvedor = ""

            data_lanc = None
            if jogo.get("first_release_date"):
                data_lanc = datetime.utcfromtimestamp(jogo["first_release_date"]).date()

            capa_url = jogo.get("cover", {}).get("url", "")
            if capa_url and capa_url.startswith("//"):
                capa_url = "https:" + capa_url
            if capa_url:
                capa_url = capa_url.replace("t_thumb", "t_cover_big")

            banner_url = ""
            if "artworks" in jogo and jogo["artworks"]:
                try:
                    banner_url = jogo["artworks"][0]["url"]
                    if banner_url.startswith("//"):
                        banner_url = "https:" + banner_url
                    banner_url = banner_url.replace("t_thumb", "t_1080p")
                except (TypeError, KeyError):
                    banner_url = ""

            trailer_url = ""
            if "videos" in jogo and jogo["videos"]:
                try:
                    video_id = jogo["videos"][0]["video_id"]
                    trailer_url = f"https://www.youtube.com/embed/{video_id}"
                except (TypeError, KeyError):
                    trailer_url = ""

            Game.objects.create(
                title=jogo.get("name", nome_jogo),
                genre=genero or "Indefinido",
                release_date=data_lanc or datetime.today().date(),
                synopsis=jogo.get("summary", ""),
                developer=desenvolvedor or "Desconhecido",
                cover_url=capa_url,
                banner_url=banner_url,
                trailer_url=trailer_url
            )
        return redirect("listar_jogos")

    return render(request, "preencher.html")


# -------------------
# Lista de jogos do usuário
# -------------------
class UserGameListView(LoginRequiredMixin, ListView):
    model = UserGameList
    template_name = "user_game_list.html"
    context_object_name = "user_games"
    paginate_by = 24

    def get_user(self):
        pk = self.kwargs.get('pk')
        if pk:
            return get_object_or_404(User, pk=pk)
        return self.request.user

    def get_queryset(self):
        user = self.get_user()
        qs = UserGameList.objects.filter(user=user).select_related('game')
        status = self.kwargs.get('status') or self.request.GET.get('status')
        if status and status != 'T':
            qs = qs.filter(status=status)
        return qs

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        user = self.get_user()
        ctx['user_profile'] = user
        ctx['current_status'] = self.kwargs.get('status') or self.request.GET.get('status', 'T')
        return ctx


# -------------------
# Views para adicionar / atualizar / remover status
# -------------------
@login_required
def add_to_list(request, game_id):
    game = get_object_or_404(Game, pk=game_id)
    obj, created = UserGameList.objects.get_or_create(
        user=request.user,
        game=game,
        defaults={'status': 'P'}
    )
    if created:
        messages.success(request, f"'{game.title}' adicionado à sua lista (Para jogar).")
    else:
        messages.info(request, f"'{game.title}' já está na sua lista.")
    return redirect(request.META.get('HTTP_REFERER', 'listar_jogos'))


@login_required
def update_game_status(request, game_id):
    if request.method == "POST":
        status = request.POST.get('status')
        if status not in dict(UserGameList.STATUS_CHOICES):
            messages.error(request, "Status inválido.")
            return redirect(request.META.get('HTTP_REFERER', '/'))

        ug, created = UserGameList.objects.update_or_create(
            user=request.user,
            game_id=game_id,
            defaults={'status': status}
        )

        if created:
            messages.success(
                request,
                f"'{ug.game.title}' adicionado à sua lista com status {ug.get_status_display()}."
            )
        else:
            messages.success(
                request,
                f"Status de '{ug.game.title}' atualizado para {ug.get_status_display()}."
            )

    return redirect(request.META.get('HTTP_REFERER', '/'))


@login_required
def remove_from_list(request, game_id):
    ug = UserGameList.objects.filter(user=request.user, game__pk=game_id).first()
    if ug:
        ug.delete()
        messages.success(request, "Jogo removido da sua lista.")
    else:
        messages.info(request, "Jogo não estava na sua lista.")
    return redirect(request.META.get('HTTP_REFERER', '/'))
