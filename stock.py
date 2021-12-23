import pandas as pd
from datetime import datetime

class Stock:
    def __init__(self):
        #Initializing Pre-Requisites
        self.url = "https://dps.psx.com.pk/market-watch"
        self.filename = "Marketdata %s.xlsx"%datetime.now().strftime('%d-%m-%Y')
        self.df = self.read_file(self.filename)

#Getting date and time to save file with it
    def get_file_data(self):
        table = pd.read_html(self.url)[0]
        self.filename = "Marketdata %s.xlsx"%datetime.now().strftime('%d-%m-%Y')
        table.to_excel(self.filename)


    def read_file(self,file):
        self.get_file_data()
        df = pd.read_excel(file)
        return df

    def get_stock(self,stock_name):
        df_stock = self.df[self.df["SYMBOL"]=="{}".format(stock_name)]
        return df_stock

    def get_stock_name(self,stock_name):
        name = self.get_stock(stock_name)
        try:
            vallist = (name["SYMBOL"].values)
            return vallist[0]
        except:
            print("No such stock as {}".format(stock_name))
            return None

    def get_stock_current_value(self,stock_name):
        name = self.get_stock(stock_name)
        try:
            vallist = (name["CURRENT"].values)
            return vallist[0]
        except:
            print("No such stock as {}".format(stock_name))
            return None

    def get_stock_change_percent(self,stock_name):
        name = self.get_stock(stock_name)
        try:
            vallist = (name["CHANGE (%)"].values)
            without_percent = vallist[0].replace('%',"")
            return float(without_percent)
        except:
            print("No such stock as {}".format(stock_name))
            return None

a = Stock()

print(a.get_stock_change_percent("TRG"))