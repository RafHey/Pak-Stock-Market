from user import User

def main():
    a = User("Raf")
    #a.add_stock("GGGL",50)
    a.save_user_to_file()

if __name__ == "__main__":
    main()