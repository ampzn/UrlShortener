import random
import string
import webbrowser
import requests


class UrlShortener:
    def __init__(self):
        self.url_dict = {}
        self.url_count = 0

    # Prompts the user to enter a URL and returns it as a string
    def user_input(self):
        url = input("Enter the URL: ")
        return url

    # Generates a random string of uppercase letters and digits with a length of 6
    def generate_short_id(self):
        short_id = "".join(random.choices(
            string.ascii_uppercase + string.digits, k=6))
        return short_id

    def shorten_url(self):
        # Prompts the user for a URL using the user_input method
        url = self.user_input()
        # Generates a short ID
        short_id = self.generate_short_id()
        # Stores the URL mapping in the url_dict dictionary
        self.url_dict[short_id] = url
        self.url_count += 1
        # Calls the is.gd API to shorten the URL
        api_url = f"https://is.gd/create.php?format=simple&url={url}"
        response = requests.get(api_url)
        if response.ok:
            short_url = response.text
            # Opens the shortened URL in a browser
            webbrowser.open(short_url)
            # Returns the shortened URL
            return short_url
        else:
            print("Error: Unable to shorten URL")
            return None

if __name__ == "__main__":
    # Creates an instance of the UrlShortener class
    shortener = UrlShortener()

    # Calls the shorten_url method to shorten the user's URL and open it in a browser
    short_url = shortener.shorten_url()
    print(short_url)