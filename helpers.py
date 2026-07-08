import requests
import json

import os
from dotenv import load_dotenv
load_dotenv()
key = os.getenv("key")

def get_movie_details(name):
    link = f"https://www.omdbapi.com/?t={name}&apikey={key}"
    try:
        response = requests.get(link)
        if response.status_code == 200:
            data = response.json()
            if data["Response"] == "True": return data
            else: raise Exception(data["Error"])
        else:
            raise Exception(f"Failed to retrieve data. Status code: {response.status_code}")
    except requests.exceptions.ConnectionError:
        print("Connect to the internet and try again")
    except Exception as e:
        print(e)