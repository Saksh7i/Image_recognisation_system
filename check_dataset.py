import os

cats_path = "dataset/cats"
dogs_path = "dataset/dogs"

cats = len(os.listdir(cats_path))
dogs = len(os.listdir(dogs_path))

print("Cat Images:", cats)
print("Dog Images:", dogs)