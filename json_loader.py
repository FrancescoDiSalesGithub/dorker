import json
import webbrowser

class JSONLoader:
    def __init__(self,page):
        self.__page = page

    def lookup(self,term):

        with open(self.__page) as json1:
            json1_string = json1.readlines()
            string = ""

        for value in json1_string:
            string = string + value

        json1 = json.loads(string)

        for value in json1['data']:
            if str(value['category']['cat_title']).find(term):
                print("{} - {} ".format(str(value['category']['cat_title']),str(value['url_title'])))