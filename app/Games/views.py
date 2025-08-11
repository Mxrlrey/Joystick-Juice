import requests
from datetime import datetime
from django.shortcuts import render, redirect
from .models import Game

# Create your views here.
def home(request):
    return render(request, 'home.html')

def listar_jogos(request):
    jogos = Game.objects.all()
    return render(request, 'listar_jogos.html', {'jogos': jogos})

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
            fields name, genres.name, first_release_date, summary, involved_companies.company.name, cover.url;
            limit 1;
        '''
        resp = requests.post("https://api.igdb.com/v4/games", headers=headers, data=body)
        resp.raise_for_status()
        dados = resp.json()

        if dados:
            jogo = dados[0]

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

            # Criar o objeto Game
            Game.objects.create(
                title=jogo.get("name", nome_jogo),
                genre=genero or "Indefinido",
                release_date=data_lanc or datetime.today().date(),
                synopsis=jogo.get("summary", ""),
                developer=desenvolvedor or "Desconhecido",
                cover_url=capa_url
            )
        return redirect("listar_jogos")

    return render(request, "preencher.html")