with open("project_book.txt", encoding = "utf-8") as read_book:
    contents = read_book.read()
    # print(count_word.lower().count("the "))
    number_words = len(contents)
    print(f"There at least {number_words} of letters")
