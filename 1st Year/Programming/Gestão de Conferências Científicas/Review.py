class Review:
    def __init__(self, reviewer_name, paper_title):
        self.__reviewer_name = reviewer_name
        self.__paper_title = paper_title
        self.__is_reviewed = False
        self.__is_approved = False
        self.__comment = ""

    def _str_(self):
        result = "Paper title: {}\nReviewer name: {}\n".format(self.paper_title, self.reviewer_name)
        result += "Reviewed: {}\nApproved: {}\n".format("yes" if self.is_reviewed else "No", "Yes" if self.is_approved else "No")
        result += "Comment: {}\n".format(self.comment)
        return result

    @property
    def reviewer_name(self):
        return self.__reviewer_name

    @property
    def paper_title(self):
        return self.__paper_title

    @property
    def is_reviewed(self):
        return self.__is_reviewed

    @property
    def is_approved(self):
        return self.__is_approved

    @property
    def comment(self):
        return self.__comment

    def result(self, is_approved, comment):
        self.__is_reviewed = True
        self.__is_approved = is_approved
        self.__comment = comment

    def print(self):
        print(self._str_())
