import telebot
from telebot import util, types
import time
from config import *
from musixmatch import *
from iso3166 import countries
from lyrics import *

bot = telebot.TeleBot(TOKEN)


@bot.message_handler(commands=["get_tracks_of"])
def tracks_of_author(message):
    author = " ".join(
        [t.capitalize() for t in message.json["text"].split(" ")[1:]]
    ).strip()
    response, status = get_tracks_of_author(author)
    if status == 200:
        ans = "Here's list of popular tracks of *" + author + "*:\n"
        for track in response["message"]["body"]["track_list"]:
            tr = track["track"]["track_name"]
            album_name = track["track"]["album_name"]
            url = track["track"]["track_share_url"]
            ans += f"Track: [{tr}]({url})\n"
            if album_name:
                ans += "Album: *" + album_name + "*"
            ans += "\n\n"
        bot.send_message(message.chat.id, text=ans, parse_mode="Markdown")
        return
    bot.send_message(
        f"Couldn't connect to MusixMatch. Please try again. Response Code: {status} Anyway you can report it to me @starboy369. Thanks!"
    )


@bot.message_handler(commands=["get_charts_of"])
def get_charts_of_country(message):
    country_code = " ".join(message.json["text"].split(" ")[1:]).strip()
    if not country_code or len(country_code) == 0:
        bot.send_message(
            message.chat.id,
            text="Please pass country code in the format of ISO3166 correctly",
        )
        return
    else:
        response, status = get_country_charts(country_code)
    if status == 200:
        answer = (
            "Here's top chart of *" + countries.get(country_code.lower()).name + "*:\n"
        )
        for track in response["message"]["body"]["track_list"]:
            tr = track["track"]["track_name"]
            artist = track["track"]["artist_name"]
            url = track["track"]["track_share_url"]
            answer += f"Track: [{tr}]({url}) (lyrics)\nArtist: *" + artist + "*\n\n"
        bot.send_message(message.chat.id, text=answer, parse_mode="Markdown")
        return
    bot.send_message(
        f"Couldn't connect to MusixMatch. Please try again. Response Code: {status} Anyway you can report it to me @starboy369. Thanks!"
    )


@bot.message_handler(commands=["get_chart_artists"])
def get_artists_of_country_chart(message):
    country_code = " ".join(message.json["text"].split(" ")[1:]).strip()
    if not country_code or len(country_code) == 0:
        bot.send_message(
            message.chat.id,
            text="Please pass country code in the format of ISO3166 correctly",
        )
        return
    else:
        response, status = get_chart_artists(country_code)
    if status == 200:
        answer = (
            "Here's artists' top chart of *"
            + countries.get(country_code.lower()).name
            + "*:\n"
        )
        print(response["message"]["body"]["artist_list"])
        for artist in response["message"]["body"]["artist_list"]:
            name = artist["artist"]["artist_name"]
            answer += f"Artist: *{name}*\n\n"
        bot.send_message(message.chat.id, text=answer, parse_mode="Markdown")
        return
    bot.send_message(
        message.chat.id,
        text=f"Couldn't connect to MusixMatch. Please try again. Response Code: {status} Anyway you can report it to me @starboy369. Thanks!",
    )


@bot.message_handler(commands=["get_lyrics"])
def get_lyrics(message):
    res = [
        tmp.strip() for tmp in "".join(message.json["text"].split(" ")[1:]).split("-")
    ]
    if len(res) == 1 and not len(res[0]):
        bot.send_message(
            message.chat.id,
            text=f"Please add searching parameters: artist name or/and track name.",
        )
        return
    elif len(res) == 1:
        track = res[0]
        artist = ''
    else:
        track, artist = res
    songs, status = search(track + " " + artist)
    if not status:
        bot.reply_to(
            message,
            text=f"Couldn't connect to MusixMatch. Please try again later. Anyway you can report it to me @starboy369. Thanks!",
        )
        return
    mkup = types.InlineKeyboardMarkup(row_width=2)
    for k in songs:
        itembtn1 = types.InlineKeyboardButton(k, callback_data=k)
        mkup.add(itembtn1)
    text = "Which song are you searching?"
    bot.send_message(message.chat.id, text, reply_markup=mkup)


@bot.callback_query_handler(func=lambda callback: True)
def callbacks(callback):
    mkup = types.InlineKeyboardMarkup(row_width=1)
    itembtn1 = types.InlineKeyboardButton("Back", callback_data="C")
    k = callback.data
    songs, status = search(k)
    if status:
        text = parse_lyrics(songs[k])
    else:
        text = "Couldn't connect to MusixMatch. Please try again later. Anyway you can report it to me @starboy369. Thanks!"
    bot.edit_message_text(
        text, callback.message.chat.id, callback.message.message_id, reply_markup=mkup
    )


@bot.message_handler()
def greet(message):
    bot.send_message(message.chat.id, text=message.json["text"])


# def polling():
#     try:
#         bot.polling()
#     except:
#         polling()
#
#
# polling()

bot.polling(none_stop=True, timeout=5)
