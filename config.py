import os

#with open("../.env", "r") as env_variables:
#    for line in env_variables.readlines():
#       k, v = line.split("=")
#        os.environ[k] = v.strip()

# dotenv.load_dotenv(".env")

BOT_TOKEN = os.environ["BOT_TOKEN"]
MUSIXMATCH_API_KEY = os.environ["MUSIXMATCH_API_KEY"]
