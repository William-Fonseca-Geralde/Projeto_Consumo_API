# pip install requests
# pip install deep_translator
# pip install pillow
# versão python 3.12.3

from deep_translator import GoogleTranslator
import tkinter as tk
from tkinter import ttk
from PIL import ImageTk, Image
import requests

class CountryLanguage:
  def __init__(self, lang):
    self.tradutor = GoogleTranslator(source= 'pt', target= 'en')
    self.lang = lang
    self.url = f"https://restcountries.com/v3.1/lang/{self.tradutor.translate(self.lang)}"
    
  def consumirAPI(self):
    response = requests.get(self.url)
    if response.status_code == 200:
      dado = response.json()
      return dado
    else:
      return "ERRO"

def mostrarDados():
  lingua = ""
  paises = CountryLanguage(lingua)
  dados = paises.consumirAPI()

janela = tk.Tk()
janela.title("Projeto Consumo de API")
janela.configure(bg="#f0f0f0")

frame = ttk.Frame(janela)
frame.pack()

texto = tk.LabelFrame(frame, text="Digite o idioma abaixo", fg= "black")
texto.grid(row=0, column=0, padx=5, pady=5)

img = Image.open("mundo.png")
nv_img = img.resize(size=(200, 75))

imagem = ImageTk.PhotoImage(nv_img)
imgFrame = tk.Label(frame, image=imagem)
imgFrame.grid(row=1, column=0, padx=5, pady=5)

resposta = ttk.Entry(texto)
resposta.insert(0, "Idioma...")
resposta.bind("<FocusIn>", lambda e: resposta.delete('0', 'end'))
resposta.grid(row=0, column=0, padx=5, pady=5, sticky='ew')

botao = ttk.Button(texto, text="Enviar".upper())
botao.grid(row=1, column=0, padx=5, pady=5, sticky="nsew")

dadosFrame = ttk.Frame(frame)
dadosFrame.grid(row=0, column=1, padx=(0, 20), pady=10)
scrollDados = ttk.Scrollbar(dadosFrame)
scrollDados.pack(side="right", fill="y")

colunas = ("Nome do país", "Nome Oficial", "Capital")
dadosView = ttk.Treeview(dadosFrame, show="headings", yscrollcommand=scrollDados.set, columns=colunas, height=15)

dadosView.column("Nome do país", width=100)
dadosView.column("Nome Oficial", width=150)
dadosView.column("Capital", width=150)
dadosView.pack()
scrollDados.config(command=dadosView.yview)


janela.mainloop()