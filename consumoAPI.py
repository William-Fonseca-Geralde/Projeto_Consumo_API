# pip install requests
# pip install deep_translator
# versão python 3.10.3

from deep_translator import GoogleTranslator
import requests

def consumirAPI(url: str):
  response = requests.get(url)
  dado = response.json()
  if response.status_code == 200:
    return dado

print("*********Descobrir Países*********")
print("1 - Pelo idioma oficial;")
print("2 - Pela região onde fica;")
print("3 - Pela subregião onde fica.")
opcao = int(input("Digite sua opção: "))

tradutor = GoogleTranslator(source= 'pt', target= 'en')

match opcao:
  case 1:
    print("Descubra todos os países de acordo com seu idioma oficial")
    lingua = input("Escreva o nome do idioma: ")
    dado = consumirAPI(f"https://restcountries.com/v3.1/lang/{tradutor.translate(lingua)}")
  case 2:
    print("Descubra quais países ficam na região")
    regiao = input("Escreva o nome da região: ")
    dado = consumirAPI(f"https://restcountries.com/v3.1/region/{tradutor.translate(regiao)}")
  case 3:
    print("Descubra quais países ficam na subregião")
    subregiao = input("Escreva o nome da subregião: ")
    dado = consumirAPI(f"https://restcountries.com/v3.1/subregion/{tradutor.translate(subregiao)}")
  case _:
    print("Digite os números pedidos acima")

tradutor = GoogleTranslator(source= 'en', target= 'pt')

for i in dado:
  print("- ",i['name']['common'])