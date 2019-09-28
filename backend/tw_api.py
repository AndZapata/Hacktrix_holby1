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
        my_list = []
        my_list2 = []
        for tweet in r.json().get('statuses'):
            try:
                print("[{}] {} by {}".format(tweet.get('id'),
                                             tweet.get('text'),
                                             tweet.get('user').get('name')))
                location = tweet.get('place').get('bounding_box').get('coordinates')
                my_neigh = buscar_location(location)
                my_list = [datetime.date,
                           datetime.time,
                           tweet.get('user').get('name'),
                           tweet.get('created_at'),
                           my_neigh]
                print("Este es my_list", my_list)
            except Exception:
                my_text = tweet.get('text')
                print(my_text)
                print("No location in tweet")
                pass
        my_list2.append(my_list)
        print (my_list2)
        return (my_list2)
    except Exception:
        print ("error")
        return None


def buscar_location(a):
    a1 = a[0][0][0]
    a2 = a[0][1][0]
    a3 = a[0][2][0]
    a4 = a[0][3][0]
    b1 = a[0][0][1]
    b2 = a[0][1][1]
    b3 = a[0][2][1]
    b4 = a[0][3][1]
    a_prom = (a1 + a2 + a3 + a4) / 4
    b_prom = (b1 + b2 + b3 + b4) / 4
    return ([a_prom, b_prom])

if __name__ == "__main__":
    doit(argv[1], argv[2], argv[3])
