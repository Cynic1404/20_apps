import requests

request = requests.get("https://www.planetware.com/wpimages/2020/02/france-in-pictures-beautiful-places-to-photograph-eiffel-tower.jpg")
a = request
b = request.text

with open("image.jpg", "wb") as file:
    file.write(request.content)