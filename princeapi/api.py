import requests


def anime_logo(name):
    API = f"https://api.princexd.tech/anime-logo?name={name}"
    req = requests.get(API).json()["url"]
    return(req)

def write(text):
    API = f"https://api.princexd.tech/write?text={name}"
    req = requests.get(API).json()["url"]
    return(req)
