import requests

# Gebruik de OMDb API 
API_KEY = "127a2880" 
url = f"http://www.omdbapi.com/?t=Fast+Five&apikey={API_KEY}"

res = requests.get(url)
data = res.json()

# Print de volledige data om te zien wat er allemaal in zit
# print(data)

# Netjes weergeven
print("----- Film Informatie -----")
print(f"Titel: {data.get('Title')}")
print(f"Jaar: {data.get('Year')}")
print(f"Regisseur: {data.get('Director')}")
print(f"Genre: {data.get('Genre')}")
print(f"IMDB-rating: {data.get('imdbRating')}")
print(f"Acteurs: {data.get('Actors')}")
print(f"Plot: {data.get('Plot')}")
print(f"Land van productie: {data.get('Country')}")
print(f"Taal: {data.get('Language')}")
print(f"Releasedatum: {data.get('Released')}")
print(f"Productie: {data.get('Production')}")
print("---------------------------")
