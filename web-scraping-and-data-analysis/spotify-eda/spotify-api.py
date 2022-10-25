#!/usr/bin/env python3
import requests
import constants

base_url = 'https://api.spotify.com/v1'

# Get artists list
headers = {
    'Authorization': constants.spotify_api_key,
    'Content-Type': 'application/json'
}
request_url = base_url + '/artists'

response = requests.get(url=request_url, headers=headers)
print(response)
