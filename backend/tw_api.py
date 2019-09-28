#!/usr/bin/python3
"""Twitter app, so much fun yay!!!!"""
import requests
from sys import argv
import base64
import datetime


def doit(apikey, secretkey, search):
    """Connects to Twitter, authenticates, and searches"""
    try:
        key = "{}:{}".format(apikey, secretkey).encode('ascii')
        key = base64.b64encode(key).decode('ascii')
        auth_headers = {
            'Authorization': 'Basic ' + key,
            'Content-Type': 'application/x-www-form-urlencoded;charset=UTF-8'
        }
        auth_data = {
            'grant_type': 'client_credentials'
        }
        r = requests.post('https://api.twitter.com/oauth2/token',
                          headers=auth_headers, data=auth_data)
        token = r.json().get('access_token')

        search_headers = {
            'Authorization': 'Bearer ' + token
        }
        search_data = {
            'q': search,
        }
        r = requests.get('https://api.twitter.com/1.1/search/tweets.json',
                         headers=search_headers, params=search_data)

        if not r.json().get('statuses'):
            return

        n = 0
        my_list = []
        for tweet in r.json().get('statuses'):
            try:
                location = tweet.get('place').get('bounding_box').get('coordinates')
#                print("este es location", location)
                my_neigh = buscar_location(location)
                my_list = [datetime.date, datetime.time, tweet.get('user')
                           .get('name'), tweet.get('created_at'), my_neigh]
                print("Esta es mi_lista", my_list)
                n += 1
            except Exception:
                pass
        return r
    except Exception:
        return None


def buscar_location(a):
    print("Este place.id", a);
    return ("Venecia")

def buscar_coordinate(a):
    return("Fontibon")

def buscar_hashtag(a):
    return("Muzu")


if __name__ == "__main__":
    doit(argv[1], argv[2], argv[3])
