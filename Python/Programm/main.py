from tkinter import *
import requests
import logging
from bs4 import BeautifulSoup

logging.basicConfig(filename='Scraper.log', level=logging.ERROR, format='%(asctime)s:%(levelname)s:%(message)s')


class Scraper(Frame):
    def __init__(self):
        super().__init__()
        self.domain = StringVar()

        self.initUI()

    def run(self):
        # GET auf die angegebene domain
        r = requests.get(self.domain.get())

        # Wenn Status-Code nicht 200 ist, dann abbrechen
        if r.status_code != 200:
            logging.error(f'Fehler beim Lesen der Daten - Fehlercode:{r.status_code}')
            exit()
        
        # HTML-Wirrwarr korrekt einrücken
        soup = BeautifulSoup(r.content, 'html.parser')
        self.result.delete("1.0", END)
        self.result.insert("1.0", soup.prettify())

    def initUI(self):
        self.master.title("Web-Scraper Test")
        self.master.geometry("1200x800")

        self.pack(fill=BOTH, expand=True)

        self.columnconfigure(1, weight=1)
        self.rowconfigure(2, weight=1)

        Label(self, text='Domain:').grid(row=0, column=0, pady=3)
        Entry(self, textvariable=self.domain).grid(row=0, column=1)
        Button(self, text='Starten', command=self.run).grid(row=1, column=0, padx=1, pady=3)

        Label(self, text='Ergebnis:').grid(row=2, column=0)

        self.result = Text(self)
        self.result.grid(row=3, column=0, columnspan=2, padx=1, pady=3)

if __name__ == "__main__":
    scraper = Scraper()
    scraper.mainloop()