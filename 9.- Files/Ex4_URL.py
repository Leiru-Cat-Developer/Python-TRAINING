# Create a function which connects with a file from internet and displays
# the number of words of the site

from urllib import request
from urllib.error import URLError

def count_words(url: str):
    try:
        link = request.urlopen(url)
    except URLError:
        print("\nThe url " + url + "doesn't exists\n")
    else:
        content = link.read()
        return len(content.split())
    
print(count_words("https://aprendeconalf.es/docencia/python/ejercicios/ficheros/"))
print(count_words("https://es.wikipedia.org/wiki/Tash_Sultana"))