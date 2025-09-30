# Write a program that opens the file with information on the GDP per capita 
# of the countries of the European Union 
# (url:https://ec.europa.eu/eurostat/estat-navtree-portlet-prod/BulkDownloadListing?
# file=data/sdg_08_10.tsv.gz&unzip=true), asks for the initials of a country and displays the 
# GDP per capita of that country for all available years.

from urllib import request
from urllib.error import URLError

def search_countries(url: str, country: str):
    try:
        with request.urlopen(url) as site:
            content = site.read.decode("utf-8").split("\n")
    except URLError:
        print(f"\nThe url doesn't exists")
    else:
        years = content.pop(0).split("\t")
        dictionary_PIB = {}
        for country in content:
            data_country = country.split("\t")
            code_country = data_country.pop(0)[-2:]
            dictionary_country = {}
            for i in range(len(data_country)):
                dictionary_country[years[i].strip()] = data_country[i].strip()
            dictionary_PIB[code_country] = dictionary_country
        return dictionary_PIB

url = ("https://ec.europa.eu/eurostat/estat-navtree-portlet-prod/"
       "BulkDownloadListing?file=data/sdg_08_10.tsv.gz&unzip=true")
country = input("\nWhat are the initials of the country: ")

search_countries(url,country)