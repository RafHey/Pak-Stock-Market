from user import User

def main():
    a = User("Testing")
    a.add_stock("TRG",200)
    #a.add_stock("BGL",100)
    #a.add_stock("GGGL",50)
    a.save_user_to_file()

if __name__ == "__main__":
    main()