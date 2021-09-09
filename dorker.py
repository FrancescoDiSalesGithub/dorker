import json
import sys

import json_loader

if __name__ == "__main__":
    
    term = sys.argv[1]
    
    json_page_1 = json_loader.JSONLoader("page1.json")
    json_page_2 = json_loader.JSONLoader("page2.json")
    json_page_3 = json_loader.JSONLoader("page3.json")
    json_page_4 = json_loader.JSONLoader("page4.json")

    json_page_1.lookup(term)
    json_page_2.lookup(term)
    json_page_3.lookup(term)
    json_page_4.lookup(term)
 
        

    