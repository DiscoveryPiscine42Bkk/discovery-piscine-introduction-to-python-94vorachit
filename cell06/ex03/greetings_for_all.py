#!/usr/bin/env python3

def greetings(word=""):
    if not word:
        print("Hello, noble stranger")
    else :
        if isinstance(word,str):
            print("Helle,", word+".")
        elif isinstance(word,int):
            print("Error! It was not a name.")

greetings('Alexandra')
greetings('Wil')
greetings(42)
greetings()