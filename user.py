from stock import Stock
import pandas as pd

class User:
    def __init__(self,name):
        self.user_name = name
        self.user_stocks = {}
        self.stock = Stock()
        #Preparing to Store direclty to Excel File of User. Currently using Driver code to generate user.
        self.df = self.get_user_file_data()
        #Updated user stocks data in code from existing sheet to avoid overwrite! BIG SUCCESS!
        self.update_user_profile()

    #Fetching Data of Current user.
    def get_user_file_data(self):
        self.filename = "Users\{}.xlsx".format(self.user_name)
        df = pd.read_excel(self.filename)
        #df1 = df.loc[df['Current Price']==143.3].values
        return df

    def add_stock(self,stock_name, quantity):
        stock_get = self.stock.get_stock_name(stock_name)
        if stock_get in self.user_stocks:
            if stock_get is not None:
                self.user_stocks[stock_get] = [self.user_stocks[stock_get][0]+quantity,self.stock.get_stock_current_value(stock_get)]
                self.bought = self.stock.get_stock_current_value(stock_get)
        else:
            if stock_get is not None: 
                self.user_stocks[stock_get] = [quantity,self.stock.get_stock_current_value(stock_get)]
                self.bought = self.stock.get_stock_current_value(stock_get) 


    def update_user_profile(self):
        for i in self.df.values:
            self.user_stocks[i[0]]=[i[1],[i[3]]]
        print(self.user_stocks)
    
    
    def print_user_profile_with_values(self):
        for i in self.user_stocks:
            print("{} : {}".format(i, self.stock.get_stock_current_value(i)))

    def return_user_profile_worth(self):
        total = 0
        for i in self.user_stocks:
            total += (self.user_stocks[i][0] * self.stock.get_stock_current_value(i))
        return(total)
    
    def print_user_profile_percentage(self):
        total_percent = 0
        for i in self.user_stocks:
            total_percent += (self.stock.get_stock_change_percent(i))
        print(total_percent)
    
    def save_user_to_file(self):
        a = {}
        b = {}
        c = {}
        d = {}
        o = {}
        l = {}
        # Create a Pandas dataframe from the data.
        if self.user_stocks != {}:
            for i in self.user_stocks:
                o[i] = self.user_stocks[i][0]
                l[i] = self.user_stocks[i][1]
                a[i] = self.stock.get_stock_current_value(i)
                b[i] = self.stock.get_stock_change_percent(i)
                c[i] = self.stock.get_stock_change(i)
                d[i] = (self.stock.get_stock_current_value(i) - self.user_stocks[i][1]) * self.user_stocks[i][0]

            df = pd.DataFrame({'Quantity': o,'Bought at':l,'Current Price': a, 'Change %': b, 'Change': c, 'Profit/Loss':d})

            # Create a Pandas Excel writer using XlsxWriter as the engine.
            writer = pd.ExcelWriter("Users\{}.xlsx".format(self.user_name), engine='openpyxl')


            # Convert the dataframe to an XlsxWriter Excel object.
            df.to_excel(writer, sheet_name='Sheet1')

            # Close the Pandas Excel writer and output the Excel file.
            writer.save()
        else:
            print("No files lmfao")
            
a = User("Raf")
# a.add_stock("TRG",50)
# a.add_stock("BWCL",500)
# a.add_stock("LMAO",1)
# a.add_stock("GGL",500)
# a.add_stock("BERG",1000)
a.print_user_profile_with_values()
print(a.return_user_profile_worth())
a.print_user_profile_percentage()
#a.add_stocks_to_profile()
a.save_user_to_file()
