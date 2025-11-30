import requests
import pandas as pd
import matplotlib.pyplot as plt

API_KEY = "127a2880"

# lijst met films (gewoon handmatig erin gezet)
films = [
    "Now You See Me 2",
    "Minions",
    "Cash Truck",
    "Fast Five",
    "Mr. Bean's Holiday",
    "Fast X",
    "Naked Gun",
    "Mission Impossible Fallout",
    "Fast & Furious 9",
    "Operation Fortune: Ruse de Guerre"
]

alle_data = []

# data ophalen voor elke film
for film in films:
    url = "http://www.omdbapi.com/?apikey=" + API_KEY + "&t=" + film.replace(" ", "+")
    r = requests.get(url)
    data = r.json()

    # Soms werkt het niet dus even checken (bijvoorbeeld als de titel niet klopt)
    if data.get("Response") == "False":
        print("Film niet gevonden:", film)
        continue

    # runtime omzetten naar getal
    runtime_txt = data.get("Runtime", "N/A")
    if runtime_txt != "N/A":
        try:
            runtime_min = int(runtime_txt.split()[0])
        except:
            runtime_min = None
    else:
        runtime_min = None

    # rating naar float
    imdb_txt = data.get("imdbRating", "N/A")
    if imdb_txt != "N/A":
        try:
            imdb_rating = float(imdb_txt)
        except:
            imdb_rating = None
    else:
        imdb_rating = None

    # opslaan in een lijst van dictionaries
    alle_data.append({
        "Title": data.get("Title"),
        "Year": data.get("Year"),
        "imdbRating": imdb_rating,
        "Runtime": runtime_min,
        "Genre": data.get("Genre")
    })

# DataFrame maken
df = pd.DataFrame(alle_data)

print("------- DataFrame -------")
print(df)

# Scatterplot maken (runtime vs rating)
df2 = df.dropna(subset=["Runtime", "imdbRating"])

plt.scatter(df2["Runtime"], df2["imdbRating"])
plt.xlabel("Runtime (min)")
plt.ylabel("IMDb rating")
plt.title("Runtime vs IMDb rating")
plt.show()

# Tabel printen
print("\n------- Tabel (Title – IMDb score – Year – Genre) -------")
print(df[["Title", "imdbRating", "Year", "Genre"]].to_string(index=False))
