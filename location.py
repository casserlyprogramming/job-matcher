
class LocationMatcher:
    def __init__(self, bio):
        self.bio = bio

    def __is_place__(self, word):
        return len(list(filter(lambda l: l.isupper(), word))) > 0

    def __get_location_from_keyword__(self, word):
        s = self.bio.split(word)
        if len(s) < 2:
            return None
        for i in range(1, len(s)):
            word = s[i].split(" ")[0]
            if self.__is_place__(word):
                return word

        return None

    def locations(self):
        excluded = []
        included = []
        in_word = self.__get_location_from_keyword__(" in ")
        out_word = self.__get_location_from_keyword__(" outside of ")
        to_word = self.__get_location_from_keyword__(" to ")
        from_word = self.__get_location_from_keyword__(" from ")
        if in_word and not to_word:
            included.append(in_word)
        if in_word and to_word:
            included.append(to_word)
            excluded.append(in_word)
        if from_word:
            included.append(from_word)
        if out_word:
            excluded.append(out_word)

        return { "included": included, "excluded": excluded }
