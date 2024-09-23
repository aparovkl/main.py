import requests
import random

def get_random_animal_image_url():    
    animal = random.randint(1, 2)
    if animal == 1:
        url = 'https://random-d.uk/api/random'
    elif animal == 2:
        url = 'https://random.dog/woof.json'
    url = url
    res = requests.get(url)
    data = res.json()
    return data['url']
