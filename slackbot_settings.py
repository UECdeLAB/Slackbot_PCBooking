# coding: utf-8
import os
from dotenv import load_dotenv

load_dotenv()

API_TOKEN = os.environ.get("SLACKBOT_API_TOKEN")
print(API_TOKEN)
PLUGINS = ['modules']