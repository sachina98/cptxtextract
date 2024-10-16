import os
from os import getenv


API_ID = int(getenv("API_ID", "28174664"))
API_HASH = getenv("API_HASH", "87c231f0e8704795b8239d06965b4351")
BOT_TOKEN = getenv("BOT_TOKEN", "7619482400:AAFGp5-uBHKUAi8Q3XE6JDl40w9HtLdAKL4")
OWNER_ID = int(getenv("OWNER_ID", "5758937746"))
SUDO_USERS = list(map(int, getenv("SUDO_USERS", "5758937746").split()))
MONGO_URL = getenv("MONGO_DB", "mongodb+srv://gathikettavan98:7Pf83ZnqV7wd4ln1@cluster0.l7v5z.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
CHANNEL_ID = int(getenv("CHANNEL_ID", "-1002387719510"))
