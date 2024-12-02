#Task2 - Create a Class Name API - RestfulBooker
#name, list_of_api , links {}
#print_apis, print_set()

class API_RestfulBooker:
    name = None
    list_of_api = []
    links = {}


    def __init__(self, name, list_of_api, links):
        self.name = name
        self.list_of_api = list_of_api
        self.links = links

    def showName(self):
        print("Name: ", self.name)

    def showList(self):
        print("List of APIs: ", self.list_of_api)

    def showLinks(self):
        print("Links: ", self.links)


obj1 = API_RestfulBooker ("Restful API Booker", ["ABC", "DEF"], {"www.abc.com", "www.pqr.in"})
obj1.showName()
obj1.showList()
obj1.showLinks()


