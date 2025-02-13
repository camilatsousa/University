class Paper:
    def __init__(self, title, authors):
        self.__title = title
        self.__authors = list(set(authors))

    def __new__(cls, *args):
        if len(args[0]) == 0:
            print("To create a paper you need a title")
            return None
        if type(args[1]) is not list:
            print("To create a paper you need a list of authors")
            return None
        if len(args[1]) < 1:
            print("To create a paper you need at least one author")
            return None
        for e in args[1]:
            if len(e) < 2:
                print("Authors names have a minimum of 2 characters")
                return None
        return object.__new__(cls)

    def __str__(self):
        result = "Title:\n    {}\nAuthors:\n    ".format(self.title)
        for e in self.authors:
            result += e + "\n    "
        return result

    def __eq__(self, other):
        if not isinstance(other, self.__class__):
            return False
        return self.title == other.title

    @property
    def title(self):
        return self.__title

    @property
    def authors(self):
        return self.__authors

    def print(self):
        print(self.__str__())
