import requests, bs4, sys, webbrowser
import json
from Parser.parser_recipe import pa
from math import *
import random

keywords = ['chicken', 'onion', 'pot roast', 'egg', 'ginger', 'chocolate', 'pasta', 'garlic', 'milk', 'walnut', 'banana', 'potato', 'spinach', 'lemon', 'cod', 'zucchini', 'egg', 'oyster', 'fish', 'crabs', 'pumpkin', 'beef', 'carrot', 'blueberries', 'cheese', 'tomato', 'noodles', 'honey', 'ham', 'celery', 'pea', 'apple', 'cabbage', 'maple syrupt', 'graham crackers', 'pepper', 'avocado', 'chili beans', 'corn', 'cornmeal', 'spaghetti', 'cocoa', 'salmon', 'tuna', 'lamb', 'mushroom', 'cinnamon', 'quinoa', 'raspberries', 'strawberries', 'pork']


def complexity(recipe):
    complex = 0
    steps = len(recipe['instructions'])
    if steps <= 3:
        complex = 1
    elif 4 <= steps <= 6:
        complex = 2
    else:
        complex = 3

    recipe["complexity"] = complex

def get_url(item):
    address = requests.get('https://www.allrecipes.com/search/results/'+item)
    address.raise_for_status()
    soup = bs4.BeautifulSoup(address.text, features="html.parser")
    recList = soup.find('ar-save-item')['data-imageurl']
    recipe = recList[1:]
    recipe = recipe[:-1]
    print(recipe)
    return recipe



def parse():
    keyword_list = []
    with open('keyword_file.txt', 'r') as f:
        for keyword in f:
            if keyword not in keyword_list:
                keyword_list.append(keyword.replace('\n', ''))
        keyword_list.remove("")
    with open('new_recipe_data.json', 'r') as json_file:
        data = json.load(json_file)
        for id in range(len(data)):
            data[str(id)]['keywords'] = []
            for item in keyword_list:
                for ing in data[str(id)]['ingredients']:
                    if item in ing:
                        data[str(id)]['keywords'].append(item)
                        break
            for ing in range(len(data[str(id)]['ingredients'])):
                data[str(id)]['ingredients'][ing] = data[str(id)]['ingredients'][ing].replace(' ADVERTISEMENT', '')

            data[str(id)]['ingredients'].remove("ADVERTISEMENT")
            pa(data[str(id)])
            complexity(data[str(id)])
            data[str(id)]['seen'] = False
            data[str(id)]['like'] = False
            data[str(id)]['id'] = id

        with open('recipe_data.json', 'w') as fp:
            json.dump(data, fp, sort_keys=False, indent=4, separators=(',', ': '))

def similar_recipes():
    with open('recipe_data.json', 'r') as json_file:
        dictionary = json.load(json_file)
        for id in range(len(dictionary)):
            dictionary[str(id)]["similar_recipes"] = []
        for id in range(len(dictionary)):
            key = str(id)
            for id2 in range(len(dictionary)):
                key2 = str(random.randint(0, len(dictionary)-1))
                #print(key2)
                count_same_words = 0
                for word in dictionary[key]["keywords"]:
                    if word in dictionary[key2]["keywords"]:
                        count_same_words += 1
                if count_same_words >= floor(len(dictionary[key]["keywords"]) / 2) and key2 not in dictionary[key]["similar_recipes"]:
                    dictionary[key]["similar_recipes"].append(key2)
                #print(dictionary[key]["similar_recipes"])
                if len(dictionary[key]["similar_recipes"]) == 5:
                    break
            if len(dictionary[key]["similar_recipes"]) == 5:
                continue
            for id2 in range(len(dictionary)):
                key2 = str(id2)
                count_same_words = 0
                for word in dictionary[key]["keywords"]:
                    if word in dictionary[key2]["keywords"]:
                        count_same_words += 1
                if count_same_words >= floor(len(dictionary[key]["keywords"]) / 2) and key2 not in dictionary[key]["similar_recipes"]:
                    dictionary[key]["similar_recipes"].append(key2)
                if len(dictionary[key]["similar_recipes"]) >= 5:
                    break
        '''for id in range(len(dictionary)):
            key = str(id)
            print(dictionary[key]["similar_recipes"])
            print(key)'''

        with open('recipe_data.json', 'w') as fp:
            json.dump(dictionary, fp, sort_keys=False, indent=4, separators=(',', ': '))


if __name__ == '__main__':
    parse()
    similar_recipes()