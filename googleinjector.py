from googlesearch import search

class googleInjector:

    def __init__(self,dork):
        self.__dork = dork
        

    def execute_dork(self):

        print("press ctrl + c when you want to stop the search")
        search_terms = search(self.__dork)

        for matches in search_terms:
            print(matches)

    def execute_dork_limit(self,limit_value):
        search_terms = search(self.__dork, num=limit_value, stop=limit_value, pause=1)

        for matches in search_terms:
            print(matches)


        