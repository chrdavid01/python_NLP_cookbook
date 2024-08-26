import requests
from bs4 import BeautifulSoup

URL = "https://americanliterature.com/author/w-w-jacobs/short-story/the-old-man-of-the-sea/"

response = requests.get(URL)

soup = BeautifulSoup(response.content, "html.parser")

story = soup.get_text()
