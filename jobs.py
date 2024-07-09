from location import LocationMatcher

class Job:
    def __init__(self, initial_data):
        self.title = initial_data["title"]
        self.location = initial_data["location"]


    def __check_individual_location__(self, locations):
        for inc in locations["included"]:
            if self.location in inc or inc in self.location:
                return True

        for exc in locations["excluded"]:
            if self.location in exc or exc in self.location:
                return False

        return None


    def search_location(self, bio):
        matcher = LocationMatcher(bio)
        locations = matcher.locations()
        if self.__check_individual_location__(locations):
            return True

        if self.__check_individual_location__(locations) == False:
            return False

        if len(locations["included"]) < 1 and len(locations["excluded"]) < 1:
            return True

        return False

    def search_title(self, bio):
        for word in bio.lower().split(" "):
            if len(word) < 4:
                continue
            if word in self.title.lower():
                print(word)
                return True
        return False
