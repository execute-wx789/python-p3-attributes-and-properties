#!/usr/bin/env python3

APPROVED_BREEDS = [
    "Mastiff",
    "Chihuahua",
    "Corgi",
    "Shar Pei",
    "Beagle",
    "French Bulldog",
    "Pug",
    "Pointer"
]

class Dog:
    def __init__(self,name="Example",breed="Pug"):
        self.name = name.title() if type(name).__name__ == "str" and len(name) < 25 and len(name) > 1 else print("Name must be string between 1 and 25 characters.")
        self.breed = breed if APPROVED_BREEDS.count(breed) == 1 else print("Breed must be in list of approved breeds.")