from bs4 import BeautifulSoup
import requests

def main(query):
	keyword=query.replace(" ","+")
	google_search="https://www.google.co.in/search?ei=wYSwW-CbNtP0rQHr2qXYCA&q={query}&oq=bubble+sort+gfg&gs_l=psy-ab.3..0i71k1l8.0.0.0.9606.0.0.0.0.0.0.0.0..0.0....0...1..64.psy-ab..0.0.0....0.tPD7PymlRjE"
	r=requests.get(google_search)


if __name__ == '__main__':
	main("Bubble sort gfg")
