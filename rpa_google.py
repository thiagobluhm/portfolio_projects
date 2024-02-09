import requests
from bs4 import BeautifulSoup

user_agent_ = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36 Edg/121.0.0.0"
query = 'python'
num_results = 10

# Alguns sites ocultam o codigo HTML pós DOM permitindo visão apenas do javascript bootstrap, para evitar isso
# devemos usar o USER-AGENT da página 
cabecalhos = {
    "user_agent_" : "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36 Edg/121.0.0.0"
}

search_url = f'https://www.google.com/search?q={query}&num={num_results}'
response = requests.get(search_url, headers=cabecalhos)

soup = BeautifulSoup(response.text, 'lxml')
# Quando se usa find estamos trazendo um Element.tag
div_main = soup.find(id="main") 
# Quando se usa find_all estamos trazendo um result element, ou uma lista que pode ser "parseada" ou percorrida por indices, no caso
# um objeto subscritable e aceitará assignment.
divs_ = div_main.find_all('div')
# Exemplo do objeto sendo indexado. Veja o print!
print(f"Primeiro índice do find_all = \n {divs_[0]}")

for div in divs_:
    print(div)
