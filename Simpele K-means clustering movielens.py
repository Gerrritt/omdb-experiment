import pandas as pd
from sklearn.cluster import KMeans

# map waar je MovieLens-bestanden staan
map_pad = r"C:\Users\remme\Desktop"

# CSV's inladen
movies = pd.read_csv(map_pad + r"\movies.csv")
ratings = pd.read_csv(map_pad + r"\ratings.csv")

print("Eerste paar films:")
print(movies.head())

print("\nEerste paar ratings:")
print(ratings.head())

# Gemiddelde rating per film
gem_ratings = ratings.groupby("movieId")["rating"].mean().reset_index()
# Aantal ratings per film
aantal_ratings = ratings.groupby("movieId")["rating"].count().reset_index()
aantal_ratings = aantal_ratings.rename(columns={"rating": "rating_count"})

# Samenvoegen met films
df = movies.merge(gem_ratings, on="movieId")
df = df.merge(aantal_ratings, on="movieId")

print("\nData met gemiddelde rating en aantal ratings:")
print(df.head())

# Alleen films met genoeg ratings (bijv. minstens 50) – anders wordt het raar
df_k = df[df["rating_count"] >= 50].copy()

print("\nData voor KMeans (minstens 50 ratings):")
print(df_k[["title", "rating", "rating_count"]].head())

# Features voor clustering: gemiddelde rating + aantal ratings
X = df_k[["rating", "rating_count"]]

# K-means model maken (3 clusters als voorbeeld)
kmeans = KMeans(n_clusters=3, random_state=0)

# Model trainen en clusters krijgen
clusters = kmeans.fit_predict(X)

# clusters opslaan
df_k["cluster"] = clusters

print("\nResultaat met clusters (eerste 50 films):")
print(df_k[["title", "rating", "rating_count", "cluster"]].head(50).to_string(index=False))

# Aantal films per cluster
print("\nAantal films per cluster:")
print(df_k["cluster"].value_counts())
