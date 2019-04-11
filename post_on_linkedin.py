import json
import requests
import os

from os.path import join, dirname
from dotenv import load_dotenv

dotenv_path = join(dirname(__file__), '.env')
load_dotenv(dotenv_path)

access_token = os.getenv('ACCESS_TOKEN')
