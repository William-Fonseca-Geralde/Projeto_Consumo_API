# pip install requests
# pip install deep_translator
# pip install pillow
# versão python 3.12.3

from deep_translator import GoogleTranslator
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
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
      return "Esse idioma não existe ou\n não tem país com esse idioma como oficial"

def mostrarDados():
  lingua = resposta.get()
  paises = CountryLanguage(lingua)
  dados = paises.consumirAPI()
  if isinstance(dados, list):
    dadosView.delete(*dadosView.get_children())
    for pais in dados:
      if 'capital' in pais:
        capital = pais['capital']
        if type(capital) == list and len(capital) > 1:
          capi = ""
          for idx, cap in enumerate(capital):
            if len(capital) - 1 != idx:
              capi += cap + ", "
            else:
              capi += cap
          capital = capi
        if type(capital) == list:
          capital = capital[0]
      else:
        capital = "Não tem"
      info = (
        pais['name']['common'],
        pais['name']['official'],
        capital
      )
      dadosView.insert('', tk.END, values=info)
      info = ()
    for nomes in colunas:
      dadosView.heading(nomes, text=nomes)
  else:
    messagebox.showinfo(title="Erro do Programa", message=dados)
    
def centralizar_tela(tela):
  screen_width = tela.winfo_screenwidth()
  screen_height = tela.winfo_screenheight()
  
  x = (screen_width - tela.winfo_reqwidth()) // 6
  y = (screen_height - tela.winfo_reqheight()) // 8

  tela.geometry("+{}+{}".format(x, y))
      
janela = tk.Tk()
janela.title("Projeto Consumo de API")
janela.configure(bg="#f0f0f0")

frame = ttk.Frame(janela)
frame.pack()

texto = tk.LabelFrame(frame, text="Digite o idioma abaixo", fg= "black")
texto.grid(row=1, column=0, padx=5, pady=5)

resposta = ttk.Entry(texto)
resposta.insert(0, "Idioma")
resposta.bind("<FocusIn>", lambda e: resposta.delete('0', 'end'))
resposta.grid(row=1, column=0, padx=5, pady=5, sticky='ew')

botao = ttk.Button(texto, text="Enviar".upper(), command=mostrarDados)
botao.grid(row=1, column=1, padx=5, pady=5, sticky="nsew")

img = Image.open("mundo.png")
nv_img = img.resize(size=(210, 110))

imagem = ImageTk.PhotoImage(nv_img)
imgFrame = tk.Label(texto, image=imagem)
imgFrame.grid(row=2, column=0,columnspan=2, padx=5, pady=5)

explicacao = tk.LabelFrame(texto, text="Explicação", fg="black")
explicacao.grid(row=1, rowspan=2, column=2, padx=45, pady=15)

textoExplic = tk.Text(explicacao, wrap="word", width=20, height=7)
textoExplic.grid(row=1, column=1, padx=10, pady=10)
textoExplic.insert(tk.END, "Nesse programa vai ser mostrado todos os países que tem o idioma oficial que você escrever na caixinha ao lado")

dadosFrame = ttk.Frame(frame)
dadosFrame.grid(row=3, column=0, padx=20, pady=10)
scrollDados = ttk.Scrollbar(dadosFrame)
scrollDados.pack(side="right", fill="y")

colunas = ("Nome do país", "Nome Oficial", "Capital")
dadosView = ttk.Treeview(dadosFrame, show="headings", yscrollcommand=scrollDados.set, columns=colunas, height=20)

dadosView.column("Nome do país", width=200)
dadosView.column("Nome Oficial", width=500)
dadosView.column("Capital", width=270)
dadosView.pack(fill="both", expand=True)
scrollDados.config(command=dadosView.yview)

centralizar_tela(janela)

janela.mainloop()