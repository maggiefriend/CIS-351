import requests
from PIL import Image
from io import BytesIO

api_key = '5NDtTamOl9fv8N1pztbK9ZdRxrfG0vtpKKl3aKuW'
rover = 'curiosity'
sol = 1000 #Martian Day
camera = 'fhaz' #Front Hazard Avoidance Camera

url = f'https://api.nasa.gov/mars-photos/api/v1/rovers/{rover}/photos'
params = {
    'sol' : sol,
    'camera' : camera,
    'api_key' : api_key

}

reponse = requests.get(url, params=params)
data = reponse.json()

if data['photos']:
    for photo in data['photos'][:2]:
        photo_url = photo['img_src']
        response = requests.get(photo_url)
        img = Image.open(BytesIO(response.content))
        img.show()
else:
    print('beep-beep, no photos found  for this rover')
