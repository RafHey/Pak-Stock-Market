from user import User

def main():
    a = User("Rafeh")
    a.add_stock("PRL",100)
    a.add_stock("PRL",200)
    a.add_stock("PRL",300)
    #a.add_stock("GGL",50)
    #a.add_stock('UNITYR3',2500)
    #a.add_stock("BGL",100)
    #a.add_stock("GGGL",50)
    a.save_user_to_file()

if __name__ == "__main__":
    main()