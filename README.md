# MusixMatchBot
## Telegram-bot

### Commands:
```
/charts <country_code> - returns top-chart of that country. 
For example: /charts usa. 
```
```
/chart_artists <country_code> - returns the list of the top artists of a given country. 
For example: /chart_artists ru
```
```
/tracks <artist_name> - returns popular tracks of given artist. 
For example: /tracks the weeknd
```
```
/lyrics <details> - returns lyrics of the track by its name and/or artist. 
For example: /lyrics bellyache billie
```

Stack: 
Python - BeautifulSoup, requests, pyTelegramBotAPI


## Deploy
```bash
git clone https://github.com/starboy-3/MusixMatch.git
cd MusixMatch/
pip install pipenv
pipenv install -r requirements.txt
pipenv python main.py
```
