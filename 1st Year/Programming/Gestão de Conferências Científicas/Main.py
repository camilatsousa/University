from Conference import Conference

conference = Conference()

lines = range(5)
options_allowed = ("1", "2", "3", "4", "5", "6", "7")
accepted_rejected = ("a", "A", "r", "R")
option = ""

while option != "7":
    for _ in lines:
        print("\n")

    print("1: Enter a new paper\n" +
          "2: Enter a new reviewer\n" +
          "3: Enter a new review.\n" +
          "4: Enter review result\n" +
          "5: Conference status\n" +
          "6: Statistics\n" +
          "7: Exit\n\n" +
          "Select an option")

    option = ""
    while not option.isnumeric():
        option = input()
        if not option.isnumeric() or option not in options_allowed:
            print("{} not recognized as an valid option".format(option))

    match option:
        case "1":
            authors = []
            print("Enter paper title")
            title = input()

            number = ""
            while not number.isnumeric():
                print("How many authors does the paper have?")
                number = input()

            for i in range(int(number)):
                print("Enter author name")
                name_author = input()
                authors.append(name_author)
            conference.new_paper(title, authors)
            print("\nEnter to continue")
            key = input()

        case "2":
            print("Enter the new reviewer name")
            reviewer_name = input()
            conference.new_reviewer(reviewer_name)
            print("\nEnter to continue")
            key = input()

        case "3":
            print("Enter the paper title")
            paper_title = input()
            print("Enter the reviewer name")
            reviewer_name = input()
            conference.new_review(paper_title, reviewer_name)
            print("\nEnter to continue")
            key = input()

        case "4":
            print("Enter the paper title")
            paper_title = input()
            print("Enter the new reviewer name")
            reviewer_name = input()
            print("Enter the review comment")
            comment = input()
            result = ""
            while result not in accepted_rejected:
                print("Is the review (A)pproved or (R)ejected?")
                result = input()
            is_approved = False
            if result == "a" or result == "A":
                is_approved = True
            conference.review_result(paper_title, reviewer_name, comment, is_approved)
            print("\nEnter to continue")
            key = input()

        case "5":
            conference.conference_status()
            print("\nEnter to continue")
            key = input()

        case "6":
            print("Average authors per paper : {}".format(conference.authors_average_per_paper()))
            print("Average reviewers per paper : {}".format(conference.reviewers_average_per_paper()))
            print("Average Paper reviewed per reviewer : {}".format(conference.paper_reviewed_average_per_reviewer()))
            conference.histogram()
            print("\nEnter to continue")
            key = input()

        case "7":
            file_name = ""
            while file_name == "":
                print("Enter file name")
                file_name = input()
            try:
                f = open(file_name, 'w')
                for e in conference.papers:
                    line = ""
                    line += e.title
                    line += ";" + str(len(e.authors))
                    for e1 in e.authors:
                        line += ";" + e1
                    line += "\n"
                    f.write(line)
                f.close()
            except IOError:
                print("Error creating file")
print("program terminated")
