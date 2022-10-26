#!/usr/bin/env python3
import json
import requests
import constants
import base64
import pandas as pd


def obtain_api_token():
    """
    An api request in order to obtain an API token to add it to request Headers.
    """
    # pull the secret keys
    client_id = constants.SPOTIFY_CLIENT_ID
    client_secret = constants.SPOTIFY_CLIENT_SECRET

    # base64 conversion
    message = f'{client_id}:{client_secret}'
    message_bytes = message.encode('ascii')
    base_64_bytes = base64.b64encode(message_bytes)
    base_64_message = base_64_bytes.decode('ascii')

    # make the request
    headers = {'Authorization': f'Basic {base_64_message}'}
    data = {'grant_type': 'client_credentials'}
    url = 'https://accounts.spotify.com/api/token'
    response = requests.post(url=url, headers=headers, data=data)
    return response.json()['access_token']


def get_artists():
    """
    A spotify API call
    to get a list of artists (needs their unique IDs for the request) with the following attributes:
        - artists: list
            a. external_urls: dict -> Known external URLs for this artist.
                - spotify: str     -> The Spotify URL for the object.
            b. followers: dict     -> Information about the followers of the artist.
                - href: str        -> This will always be set to null, as the Web API does not support it at the moment.
                - total: int       -> The total number of followers.
            c. genres: list        -> A list of the genres the artist is associated with. 
                                      If not yet classified, the array is empty.
            d. href: str           -> A link to the Web API endpoint providing full details of the artist.
            e. id: str             -> The Spotify ID for the artist.
            f. images: list        -> Images of the artist in various sizes, widest first.
                - url: str         -> The source URL of the image.
                - height: int      -> The image height in pixels.
                - width: int       -> The image width in pixels.
            g. name: str           -> The name of the artist.
            h. popularity: int     -> The popularity of the artist.
                                      The value will be between 0 and 100, with 100 being the most popular. 
                                      The artist's popularity is calculated from the popularity of all the artist's tracks.
            i. type: str           -> The object type.
            j. uri: str            -> The Spotify URI for the artist.
    """
    # prepare data for the request
    token = obtain_api_token()
    ids = "3TVXtAsR1Inumwj472S9r4,2CIMQHirSU0MQqyYHq0eOx,57dN52uHvrHOxijzpIgu3E,1vCWHaC5f2uS3yhpwWbIA6,1RyvyyTE3xzB2ZywiAwp0i,0Y5tJX1MQlPlqiwlOH1tJY,3b8QkneNDz4JHKKKlLgYZg,3wyVrVrFCkukjdVIdirGVY,2kCcBybjl3SAtIcwdWpUe3"
    url = f'https://api.spotify.com/v1/artists/?ids={ids}'
    headers = {
        'Authorization': f'Bearer {token}',
        'Content-Type': 'application/json'
    }

    # make the request
    response = requests.get(url=url, headers=headers)
    json_data = json.dumps(response.json()['artists'], indent=2)
    df = pd.read_json(json_data)
    df.to_csv('./data/artists_data.csv', index=None)


if __name__ == '__main__':
    get_artists()
