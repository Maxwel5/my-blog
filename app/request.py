import requests
from config import Config
from .models import Quotes

new_quotes_url = 'http://quotes.stormconsultancy.co.uk/random.json'

def getQuotes():
   random_quote = requests.get(new_quotes_url)
   new_quote = random_quote.json()
   author = new_quote.get("author")
   quote = new_quote.get("quote")
   permalink = new_quote.get("permalink")
   quote_all = Quotes(author,quote,permalink)
   return quote_all