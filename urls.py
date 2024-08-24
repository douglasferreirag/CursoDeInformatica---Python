
from googlesearch import search

pesquisa = input("Digite o que deseja pesquisar: ")

for url in search(pesquisa, stop=20):
    print(url)