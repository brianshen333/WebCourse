from Grep import Grep

class Application:
    def run():
        while True:
            try:

                print("Please enter location of the favourite.fav file. Ex: C:/Users/Brian/OneDrive/Desktop/FavouriteGrep/favourite.fav")
                location = input("location : ")
                email = input("Please enter email to be deleted : ")
                instance = Grep(location,email)
            except FileNotFoundError:
                print("file doesn't exist. Please check file location and use backslash / ")
            except SyntaxError:
                print("Please use backslash to as seperator in file location. Ex: C:/Users/Brian/OneDrive/Desktop/FavouriteGrep/favourite.fav")