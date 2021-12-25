import requests
from bs4 import BeautifulSoup
from bs4 import Comment

search_url = "https://search.azlyrics.com/search.php?q="


def search(parameter, timeout=None):
    req_url = search_url + parameter
    try:
        response = requests.get(req_url, timeout)
        soup = BeautifulSoup(response.content, "html.parser")
    except:
        return {}, False
    songs = {}
    soup = soup("div", "panel")
    if len(soup) < 1:
        return {"Error": "Please pass track name more correctly."}, False
    for tr in soup[0].table:
        if tr == "\n":
            continue
        bs = tr.find_all("b")
        if len(bs) > 1:
            track = str(bs[0].text.replace('"', ""))
            artist = str(bs[1].text)
            songs[artist + " - " + track] = tr.td.a["href"]
    return songs, True


def parse_lyrics(url, timeout=None):
    response = requests.get(url, timeout)
    soup = BeautifulSoup(response.content, "html.parser")
    soup = soup("div", class_="")[1]
    for element in soup(text=lambda text: isinstance(text, Comment)):
        element.extract()
    lyrics = soup.text.strip()
    return lyrics
