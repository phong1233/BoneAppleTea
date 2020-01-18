import re

def parser(recipe):
       steps = recipe["ingredients"]
       ingredients_array = re.split('\n', steps)
       recipe["ingredients"] = ingredients_array


def add_keyword(new_keyword):
    file = open("keyword_file.txt", "r+")

    keywords = file.read()
    keywords_list = re.split('\n', keywords)
    for keyword in keywords_list:
        if keyword == new_keyword:
            return

    file.write("\n" + new_keyword)

    file.close()

