import requests
import json
from config import mmatch_api

URL = "https://api.musixmatch.com/ws/1.1/"


def get_tracks_of_author(author, page_size=3):
    parameters = (
        "track.search?q_artist="
        + author
        + "&page_size="
        + str(page_size)
        + "s_artist_rating=desc&s_track_rating=desc&quorum_factor=1"
    )
    req_url = URL + parameters + "&apikey=" + mmatch_api
    response = requests.get(
        req_url,
    )
    if response.status_code == 200:
        x = json.loads(response.content)
        return x, response.status_code
    return f"Error! Something went wrong.", response.status_code


def get_country_charts(country_code="XW", page_size=3):
    parameters = (
        "chart.tracks.get?country="
        + country_code
        + "&page_size="
        + str(page_size)
        + "&apikey="
        + mmatch_api
    )
    req_url = URL + parameters
    response = requests.get(req_url)
    if response.status_code == 200:
        x = json.loads(response.content)
        return x, response.status_code
    return f"Error! Something went wrong.", response.status_code


def get_chart_artists(country_code="US", page=1, artists_num=3):
    # This api provides you the list of the top artists of a given country.
    parameters = (
        "chart.artists.get?page="
        + str(page)
        + "&page_size="
        + str(artists_num)
        + "&country="
        + country_code.lower()
        + "&apikey="
        + mmatch_api
    )
    req_url = URL + parameters
    response = requests.get(req_url)
    if response.status_code == 200:
        x = json.loads(response.content)
        return x, response.status_code
    return f"Error! Something went wrong.", response.status_code
