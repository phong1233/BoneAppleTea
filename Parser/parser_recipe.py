import re


def pa(recipe):
       steps = recipe["instructions"]
       ingredients_array = re.split('\n', steps)
       recipe["instructions"] = ingredients_array
       while "" in ingredients_array:
           ingredients_array.remove("")


def add_keyword(new_keyword):
    file = open("keyword_file.txt", "r+")

    keywords = file.read()
    keywords_list = re.split('\n', keywords)
    for keyword in keywords_list:
        if keyword == new_keyword:
            return

    file.write("\n" + new_keyword)

    file.close()

def get_new_keyword():
    user_input = ""
    while user_input != "quit":
        add_keyword(user_input)
        user_input = input("Enter new keyword: ")

