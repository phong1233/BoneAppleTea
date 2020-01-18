import re

def parser(recipe):
       steps = recipe["ingredients"]
       ingredients_array = re.split('\n', steps)
       recipe["ingredients"] = ingredients_array


def add_keyword(new_keyword):
    file = open("keyword_file.txt", "a")
    keywords
    for keyword in keywords:
        if keyword == new_keyword:
            return
    keywords.append(new_keyword)


