from requests import Request, Session
from requests.exceptions import ConnectionError, Timeout, TooManyRedirects
from tkinter import Tk, Label, Button, StringVar

url = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/listings/latest'

parameters = {
    'start':'1',
    'limit':'1',
    'convert':'USD'
}

headers = {
  'Accepts': 'application/json',
  'X-CMC_PRO_API_KEY': 'b2efde48-45e0-4d50-8722-4eef203b7373',
}

session = Session()
session.headers.update(headers)


class MyFirstGUI:
    def __init__(self, master):
        self.master = master
        master.geometry("400x100")
        master.title("Check BTC!")

        self.label_text = StringVar()
        self.label_text.set("Btc: $")
        self.label = Label(master, textvariable=self.label_text)
        self.label.pack()

        self.btc_button = Button(master, text="Check BTC", bg='black', fg='red', command=self.checkBtc)
        self.btc_button.pack()

    def checkBtc(self):
        try:
            response = session.get(url, params=parameters)
            response_json = response.json()
            print(response_json['data'][0]['quote']['USD']['price'])
            self.label_text.set("Btc: "+str(response_json['data'][0]['quote']['USD']['price'])+"$")
            root.update_idletasks()
        except (ConnectionError, Timeout, TooManyRedirects) as e:
            print("e")


root = Tk()
my_gui = MyFirstGUI(root)
root.mainloop()