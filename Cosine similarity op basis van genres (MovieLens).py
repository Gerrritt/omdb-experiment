import pandas as pd
import numpy as np
from sklearn.metrics.pairwise import cosine_similarity

# map waar de MovieLens bestanden staan
map_pad = r"C:\Users\remme\Desktop"

# movies.csv inladen
movies = pd.read_csv(map_pad + r"\movies.csv")

print("Eerste paar films:")
print(movies.head())

# We nemen alleen een subset (bijv. de eerste 20 films) om het simpel te houden
# Dit kun je later aanpassen
subset = movies.head(20).copy()

print("\nSubset van films:")
print(subset[["movieId", "title", "genres"]])

# Alle unieke genres verzamelen
alle_genres = []

for gen in subset["genres"]:
    # genres staan meestal zo: "Action|Adventure|Sci-Fi"
    losse = str(gen).split("|")
    for g in losse:
        g_schoon = g.strip()
        if g_schoon != "(no genres listed)" and g_schoon not in alle_genres:
            alle_genres.append(g_schoon)

print("\nAlle genres in subset:")
print(alle_genres)

# Matrix maken: rij = film, kolom = genre (0/1)
matrix = []

for i, rij in subset.iterrows():
    gen = str(rij["genres"]).split("|")
    gen = [x.strip() for x in gen]

    vector = []
    for g in alle_genres:
        if g in gen:
            vector.append(1)
        else:
            vector.append(0)
    matrix.append(vector)

genre_matrix = np.array(matrix)

# Cosine similarity berekenen
sim = cosine_similarity(genre_matrix)

print("\nCosine similarity matrix (genres):")
print(sim)

# Meest vergelijkbare film per film
print("\nMeest vergelijkbare film per film (op basis van genres):")

titels = list(subset["title"])

for i in range(len(titels)):
    scores = list(sim[i])
    scores[i] = -1  # zichzelf uitsluiten

    beste_index = scores.index(max(scores))
    beste_score = scores[beste_index]

    print(f"'{titels[i]}' lijkt het meest op '{titels[beste_index]}' (score = {beste_score:.2f})")
