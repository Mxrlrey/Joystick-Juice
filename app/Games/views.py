import requests
from datetime import datetime
from django.views.generic import CreateView, ListView, DeleteView, UpdateView, DetailView

from .models import Game

from django.shortcuts import render, get_object_or_404, redirect
from Reviews.models import Review, Comment
from Reviews.forms import CommentForm
from django.contrib.auth.decorators import login_required

# Create your views here.
def home(request):
    games = Game.objects.all() 
    return render(request, 'home.html', {'games': games})

def listar_jogos(request):
    jogos = Game.objects.all()
    return render(request, 'listar_jogos.html', {'jogos': jogos})

class games(DetailView):
    model = Game
    template_name = 'games.html'

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

        # Ajustar campos para buscar gênero, desenvolvedor, etc
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

            for game in Game.objects.all():
                if game.title.lower() == jogo.get("name", "").lower():
                    # Jogo já existe, não duplicar
                    return redirect("listar_jogos")

            # Extrair gênero (pode ser lista, vamos pegar o primeiro ou vazio)
            genero = ""
            if "genres" in jogo and jogo["genres"]:
                # genres é lista de IDs, mas aqui buscamos nome direto
                # às vezes pode ser necessário buscar numa outra chamada se vier só id
                try:
                    genero = jogo["genres"][0]["name"]
                except (TypeError, KeyError):
                    genero = ""

            # Extrair desenvolvedor (envolvido em involved_companies, buscar o primeiro)
            desenvolvedor = ""
            if "involved_companies" in jogo and jogo["involved_companies"]:
                try:
                    desenvolvedor = jogo["involved_companies"][0]["company"]["name"]
                except (TypeError, KeyError):
                    desenvolvedor = ""

            # Converter timestamp para date
            data_lanc = None
            if jogo.get("first_release_date"):
                data_lanc = datetime.utcfromtimestamp(jogo["first_release_date"]).date()

            # Ajustar URL da capa (a IGDB retorna algo tipo "//images.igdb.com/...")
            capa_url = jogo.get("cover", {}).get("url", "")
            if capa_url and capa_url.startswith("//"):
                capa_url = "https:" + capa_url

            if capa_url:
                capa_url = capa_url.replace("t_thumb", "t_cover_big")

            # Banner / artwork (pegar o primeiro, se existir)
            banner_url = ""
            if "artworks" in jogo and jogo["artworks"]:
                try:
                    banner_url = jogo["artworks"][0]["url"]
                    if banner_url.startswith("//"):
                        banner_url = "https:" + banner_url
                    banner_url = banner_url.replace("t_thumb", "t_1080p")  # maior resolução
                except (TypeError, KeyError):
                    banner_url = ""

            # Trailer (YouTube)
            trailer_url = ""
            if "videos" in jogo and jogo["videos"]:
                try:
                    video_id = jogo["videos"][0]["video_id"]
                    trailer_url = f"https://www.youtube.com/embed/{video_id}"  # link embed
                except (TypeError, KeyError):
                    trailer_url = ""



            # Criar o objeto Game
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

def game_detail(request, game_id):
    # pega o game
    game = get_object_or_404(Game, pk=game_id)

    # pega todas as reviews do game
    reviews = Review.objects.filter(game=game).order_by('-reviewID')

    # comentário novo
    if request.method == 'POST':
        form = CommentForm(request.POST)
        review_id = request.POST.get('review_id')
        review = get_object_or_404(Review, pk=review_id)
        if form.is_valid() and request.user.is_authenticated:
            comment = form.save(commit=False)
            comment.user = request.user
            comment.review = review
            comment.save()
            return redirect('game_detail', game_id=game_id)
    else:
        form = CommentForm()

    return render(request, 'games/game_detail.html', {
        'object': game,
        'reviews': reviews,
        'form': form
    })