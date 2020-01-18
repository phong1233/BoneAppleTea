import requests, bs4, sys, webbrowser
import json
from Parser.parser_recipe import pa

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
                keyword_list.append(keyword)
    with open('new_recipe_data.json', 'r') as json_file:
        data = json.load(json_file)
        for id in range(len(data)):
            for item in keyword_list:
                for ing in data[str(id)]:
                    if item in ing:
                        data[str(id)]['keywords'].append(item)
                        break
            for ing in range(len(data[str(id)]['ingredients'])):
                data[str(id)]['ingredients'][ing].replace(' ADVERTISEMENT', '')

            pa(data[str(id)])
            complexity(data[str(id)])
            data[str(id)]['seen'] = False
            data[str(id)]['like'] = False

        with open('recipe_data.json', 'w') as fp:
            json.dump(data, fp, sort_keys=True, indent=4, separators=(',', ': '))

if __name__ == '__main__':
    parse()