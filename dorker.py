import sys

import json_loader
import googleinjector
import graphics

if __name__ == "__main__":
    
    term = sys.argv[1]
    visuals = graphics.graphics()

    if len(sys.argv) <= 2 and (term == "help" or term == "--help"):
        visuals.disclaimer()
        visuals.doBanner()
        visuals.print_help()
        sys.exit(0)

    if len(sys.argv) == 3:
        command = sys.argv[2]
        visuals.disclaimer()
        visuals.doBanner()

        if term == "search":
            json_page_1 = json_loader.JSONLoader("page1.json")
            json_page_2 = json_loader.JSONLoader("page2.json")
            json_page_3 = json_loader.JSONLoader("page3.json")
            json_page_4 = json_loader.JSONLoader("page4.json")

            json_page_1.lookup(command)
            json_page_2.lookup(command)
            json_page_3.lookup(command)
            json_page_4.lookup(command)

        if term == "execute":
            injector = googleinjector.googleInjector(command)
            injector.execute_dork()
 
        if term == "executelimit":
            limit_value_search = int(input("how many values do you want to search? "))

            injector = googleinjector.googleInjector(command)
            injector.execute_dork_limit(limit_value_search)
    else:
        visuals.disclaimer()
        visuals.doBanner()
        visuals.print_help() 

    