import urllib.request, json 
import tkinter as tk
from datetime import date

waluta=0
liczba=0

root = tk.Tk()
root.geometry("1100x500")
Kalkulator = tk.Label(root, text='Kalkulator Walut',  fg= 'black', font=("bold", 30, "italic"))
Kalkulator.grid(row=1 )
Kalkulator.place(relx=0.5, rely=0.090, anchor=tk.CENTER)
textbox1 = tk.Entry(root, textvariable=liczba,font=('Times', 24))
textbox1.place(relx=0.2, rely=0.490, anchor=tk.CENTER, width=256, height= 50)
Blok_autorstwa = tk.Label(root, text='Kamil Janowski 3TPA',  fg= 'black', font=("bold", 30, "italic"))
Blok_autorstwa.grid(row=1 )
Blok_autorstwa.place(relx=0.5, rely=0.890, anchor=tk.CENTER)
def wybrana_metoda():
     e_text=textbox1.get()
     message3.config(text= str(e_text)+"zł")
def ustaw_euro():
     waluta="EUR"
     with urllib.request.urlopen("https://api.nbp.pl/api/exchangerates/rates/a/"+str(waluta)+"/"+str(date.today())+"/?format=json") as url:
      data = json.load(url)
      e_text=textbox1.get()
      kurs=data['rates'] [0] ['mid']
      finalowa_liczba=float(e_text)
      print(finalowa_liczba * float(kurs))
      final=(float(e_text) * float(kurs))
      message3.config(text= str(round(final,2))+"zł")
     
def ustaw_USD():
     waluta="USD"
     with urllib.request.urlopen("https://api.nbp.pl/api/exchangerates/rates/a/"+str(waluta)+"/"+str(date.today())+"/?format=json") as url:
      data = json.load(url)
      e_text=textbox1.get()
    
      kurs=data['rates'] [0] ['mid']
      print(float(e_text) * float(kurs))
      final=(float(e_text) * float(kurs))
      message3.config(text= str(round(final,2))+"zł")
def ustaw_CHF():
     waluta="CHF"
     with urllib.request.urlopen("https://api.nbp.pl/api/exchangerates/rates/a/"+str(waluta)+"/"+str(date.today())+"/?format=json") as url:
      data = json.load(url)
      e_text=textbox1.get()
    
      kurs=data['rates'] [0] ['mid']
      print(float(e_text) * float(kurs))
      final=(float(e_text) * float(kurs))
      message3.config(text= str(round(final,2))+"zł")
     
     
USD_BUTTON = tk.Button(root, text ="USD",command=ustaw_USD )
USD_BUTTON.place(relx=0.450, rely=0.290, anchor=tk.CENTER, width=256, height= 50)
EURO_BUTTON = tk.Button(root, text ="EURO",command=ustaw_euro )
EURO_BUTTON.place(relx=0.450, rely=0.490, anchor=tk.CENTER, width=256, height= 50)
CHF_BUTTON = tk.Button(root, text ="CHF",command=ustaw_CHF )
CHF_BUTTON.place(relx=0.450, rely=0.690, anchor=tk.CENTER, width=256, height= 50)
message3 = tk.Label(root,   fg= 'black', font=("bold", 30, "italic"))
message3.grid(row=1 )
message3.place(relx=0.8, rely=0.530, anchor=tk.CENTER)




print('Przelicznik Walut')



#http://api.nbp.pl/api/exchangerates/rates/a/{waluta}/{dzien}/?format=json"}
#https://api.nbp.pl/api/exchangerates/rates/a/usd/2023-05-09/?format=json


root.mainloop()