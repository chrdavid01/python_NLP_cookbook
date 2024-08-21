import requests
from bs4 import BeautifulSoup

URL = "https://servicioskoinonia.org/cuentoscortos/articulo.php?num=046"

response = requests.get(URL)

soup = BeautifulSoup(response.content, "html.parser")

story = soup.get_text()
