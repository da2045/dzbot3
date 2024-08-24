import requests


def get_random_dog():
    endpoint_dog = 'https://dog.ceo/api/breeds/image/random'
    response = requests.get(endpoint_dog)
    data = response.json()
    return data['message']

def get_random_picture(category):
    endpoint_nature = 'https://dog.ceo/api/breeds/image/random'
    response = requests.get(endpoint_nature)
    data = response.json()
    return data['message']