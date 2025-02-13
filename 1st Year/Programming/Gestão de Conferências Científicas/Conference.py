from Paper import Paper
from Review import Review
import matplotlib.pyplot as plt
import numpy


class Conference:

    def __init__(self):
        self.__reviewers = []
        self.__papers = []
        self.__reviews = []

    @property
    def papers(self):
        return self.__papers

    def new_paper(self, title, authors):
        if self.paper_exist_by_title(title):
            print("\nA paper with this title already exists")
            return
        paper = Paper(title, authors)
        if paper:
            self.__papers.append(paper)
            print("\nnew paper added")

    def new_reviewer(self, name):
        if len(name) < 2:
            print("\nThe reviewer name have a minimum of 2 characters")
            return
        if self.reviewer_exist_by_name(name):
            print("\nThis reviewer already exists")
        else:
            self.__reviewers.append(name)

    def new_review(self, paper_title, reviewer_name):
        # ver se existe um paper com titulo de paper_title
        if self.get_paper_by_title(paper_title) is None:
            print("\nYou are trying to create a review for a paper that hasn't been added")
            return

        # ver se existe revisor com nome reviewer_name
        if not self.reviewer_exist_by_name(reviewer_name):
            print("\nYou are trying to create a review from a reviewer that hasn't been added to the system")
            return

        if self.get_review(paper_title, reviewer_name):
            print("\nA review with the same paper title and the same reviewer name already exists")
            return

        review = Review(reviewer_name, paper_title)
        if review:
            self.__reviews.append(review)
            print("\nNew review added")

    def review_result(self, paper_title, reviewer_name, comment, is_approved):
        if not self.__reviews:
            print("\nYou need to create reviews first")
            return

        paper = self.get_paper_by_title(paper_title)
        if paper is None:
            print("\nThat paper doesn't exist")
            return

        if not self.reviewer_exist_by_name(reviewer_name):
            print("\nThat reviewer doesn't exist")
            return

        review = self.get_review(paper_title, reviewer_name)
        if review is None:
            print("\nThat review doesn't exist")
            return
        else:
            if review.is_reviewed:
                print("\nThis review is already completed")
                return
        review.result(is_approved, comment)
        print("\nResult added - Review Completed")

    def get_paper_by_title(self, title):
        if self.__papers:
            for e in self.__papers:
                if e.title == title:
                    return e
        return None

    def get_review(self, paper_title, reviewer_name):
        if self.__reviews:
            for e in self.__reviews:
                if e.paper_title == paper_title and e.reviewer_name == reviewer_name:
                    return e
        return None

    def count_papers(self):
        return len(self.__papers)

    def count_reviewers(self):
        return len(self.__reviewers)

    def count_incomplete_reviews(self):
        n = 0
        for e in self.__reviews:
            if not e.is_reviewed:
                n += 1
        return n

    def paper_exist_by_title(self, paper_title):
        element = self.get_paper_by_title(paper_title)
        return False if element is None else True

    def reviewer_exist_by_name(self, reviewer_name):
        return reviewer_name in self.__reviewers

    def review_exist_by_name_and_title(self, reviewer_name, paper_title):
        element = self.get_paper_by_title(paper_title)
        if element is not None and self.reviewer_exist_by_name(reviewer_name):
            return True
        else:
            return False

    def is_reviewed_by_reviewer_completed(self, paper_title, reviewer_name):
        element = self.get_review(paper_title, reviewer_name)
        if element is None:
            print("That review doesn't exist")
        return True if element.is_reviewed else False

    def is_paper_approved_by_reviewer(self, paper_title, reviewer_name):
        element = self.get_review(paper_title, reviewer_name)
        if element is None:
            print("That review doesn't exist")
        return True if element.is_approved else False

    def is_paper_approved(self, paper_title):
        if self.get_paper_by_title(paper_title) is not None:  # vê se existe o paper
            total = 0
            reviewed = 0
            approved = 0
            for e in self.__reviews:
                if e.paper_title == paper_title:
                    total += 1
                    if e.is_reviewed:
                        reviewed += 1
                    if e.is_approved:
                        approved += 1
            return True if (total == reviewed and reviewed == approved and reviewed != 0) else False
        return False

    def is_paper_is_rejected(self, paper_title):
        if self.get_paper_by_title(paper_title) is not None:
            total = 0
            reviewed = 0
            approved = 0
            for e in self.__reviews:
                if e.paper_title == paper_title:
                    total += 1
                    if e.is_reviewed:
                        reviewed += 1
                    if e.is_approved:
                        approved += 1
            return True if (total == reviewed and approved < reviewed) else False
        return False

    def is_paper_not_fully_reviewed(self, paper_title):
        if self.get_paper_by_title(paper_title) is not None:
            total = 0
            reviewed = 0
            for e in self.__reviews:
                if e.paper_title == paper_title:
                    total += 1
                    if e.is_reviewed:
                        reviewed += 1
                return True if total > reviewed else False

    def get_papers_without_reviews_associated(self):
        papers_titles = []
        for e in self.__papers:
            papers_titles.append(e.title)
        for e1 in self.__papers:
            for e2 in self.__reviews:
                if e1.title == e2.paper_title and e1.title in papers_titles:
                    papers_titles.remove(e1.title)
        if papers_titles:
            for e in papers_titles:
                print("   {}".format(e))
        else:
            print("    *none")

    def get_paper_reviews(self, title):
        for e in self.__reviews:
            if e.paper_title == title:
                e.print()

    def conference_status(self):
        print("**Accepted Papers: ")
        count = 0
        for e in self.__papers:
            if self.is_paper_approved(e.title):
                e.print()
                count += 1
        if count == 0:
            print("    *none")
        print("**Rejected Papers: ")
        count = 0
        for e in self.__papers:
            if self.is_paper_is_rejected(e.title):
                e.print()
                count += 1
        if count == 0:
            print("    *none")
        print("**Unreviewed Papers: ")
        self.get_papers_without_reviews_associated()

    # Statistics
    def authors_average_per_paper(self):
        count = 0
        for e1 in self.__papers:
            for _ in e1.authors:
                count += 1
        return count / self.count_papers() if self.count_papers() != 0 else 0

    def reviewers_average_per_paper(self):
        return self.count_reviewers() / self.count_papers() if self.count_papers() != 0 else 0

    def paper_reviewed_average_per_reviewer(self):
        complete_reviews = len(self.__reviews) - self.count_incomplete_reviews()
        return complete_reviews / self.count_reviewers() if self.count_reviewers() != 0 else 0

    def histogram(self):
        # neste caso, da-me jeito utilizar um dicionario
        # fico com a contagem de revioes por cada revisor
        count_per_reviewer = {}
        for e in self.__reviewers:
            count = 0
            for e1 in self.__reviews:
                if e == e1.reviewer_name:
                    count += 1
            count_per_reviewer[e] = count
        # crio uma lista com a quantidade de reviews de cada reviewer
        list_of_results = []
        for i in count_per_reviewer:
            list_of_results.append(count_per_reviewer[i])
        # crio um set da lista
        no_repeats_list = set(list_of_results)
        # o tamanho do set define a quantidade de linhas que preciso no array
        mydata = numpy.zeros([len(no_repeats_list), 2], int)
        # googlei para usar o for com possibilidade de reter o indice do elemento
        for idx, e in enumerate(no_repeats_list):
            count = 0
            for j in list_of_results:
                if e == j:
                    count += 1
            # guardo no array a quantidade de reviews
            mydata[idx, 0] = e
            # e a quantidade de reviewers associados a essa quantidade de review
            mydata[idx, 1] = count
        print(mydata)
        labels = [str(i) + " Reviews" for i in mydata[:, 0]]
        plt.bar(labels, mydata[:, 1])
        plt.show()
