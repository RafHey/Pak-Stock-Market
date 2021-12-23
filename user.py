from stock import Stock
import pandas as pd

class User:
    def __init__(self,name):
        self.user_name = name
        self.user_stocks = {}
        self.stock = Stock()
    
    def add_stock(self,stock_name, quantity):
        stock_get = self.stock.get_stock_name(stock_name)
        if stock_get in self.user_stocks:
            if stock_get is not None:
                self.user_stocks[stock_get] += quantity
        else:
            if stock_get is not None: 
                self.user_stocks[stock_get] = quantity


    def print_user_profile(self):
        print("{} has".format(self.user_name))
        print(self.user_stocks)
    
    
    def print_user_profile_with_values(self):
        for i in self.user_stocks:
            print("{} : {}".format(i, self.stock.get_stock_current_value(i)))

    def print_user_profile_worth(self):
        total = 0
        for i in self.user_stocks:
            total += (self.user_stocks[i] * self.stock.get_stock_current_value(i))
        print(total)
    
    def print_user_profile_percentage(self):
        total_percent = 0
        for i in self.user_stocks:
            total_percent += (self.stock.get_stock_change_percent(i))
        print(total_percent)
    
    def save_user_to_file(self):
        a = {}
        b = {}
        c = {}
        # Create a Pandas dataframe from the data.
        for i in self.user_stocks:
            a[i] = self.stock.get_stock_current_value(i)
            b[i] = self.stock.get_stock_change_percent(i)
            c[i] = self.stock.get_stock_change_percent(i)
        df = pd.DataFrame({'Quantity': self.user_stocks, 'Current Price': a, 'Change %': b})

        # Create a Pandas Excel writer using XlsxWriter as the engine.
        writer = pd.ExcelWriter('{}.xlsx'.format(self.user_name), engine='xlsxwriter')


        # Convert the dataframe to an XlsxWriter Excel object.
        df.to_excel(writer, sheet_name='Sheet1')

        # Close the Pandas Excel writer and output the Excel file.
        writer.save()
        
a = User("Rafeh")
a.add_stock("TRG",50)
a.add_stock("BWCL",500)
a.add_stock("LMAO",1)
a.add_stock("BERG",1000)
a.print_user_profile()
a.print_user_profile_with_values()
a.print_user_profile_worth()
a.print_user_profile_percentage()
#a.add_stocks_to_profile()
a.save_user_to_file()
