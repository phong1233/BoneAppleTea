import requests, bs4, sys, webbrowser
import json
import parser

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


def parse_json():
    new_data = {}
    count = 1000
    with open('recipes_raw_nosource_ar.json') as json_file:
        data = json.load(json_file)
        recipe_id = 0
        for d in data:
            try:
                print(str(recipe_id) + " " + d)
                new_data[recipe_id] = data[d]
                new_data[recipe_id]['picture_link'] = get_url(data[d]['title'])
                '''c = 0
                l = len(ingredients)
                key_ingredients = []
                for item in ingredients:
                    if_in = is_in(item)
                    if if_in != 'nothing':
                        if if_in not in key_ingredients:
                            key_ingredients.append(if_in)
                    new_data[recipe_id]['ingredients'].append(item.replace(' ADVERTISEMENT', ''))
                    c += 1
                    if c == l - 1:
                        break
                new_data[recipe_id]['keywords'] = []
                for i in key_ingredients:
                    new_data[recipe_id]['keywords'].append(i)'''

                if count == 0:
                    break
                count -= 1
                recipe_id += 1
            except Exception:
                recipe_id -= 1
                new_data.pop(recipe_id)

    with open('new_recipe_data.json', 'w') as fp:
        json.dump(new_data, fp, sort_keys=True, indent=4, separators=(',', ': '))


def add_keywords(keyword_file, dataset):
    keyword_list = []
    with open(keyword_file, 'r') as f:
        for keyword in f:
            if keyword not in keyword_list:
                keyword_list.append(keyword)
    new_data = {}
    with open(dataset) as json_file:
        data = json.load(json_file)
        recipe_id = 0
        for d in data:

            c = 0
            l = len(keyword_list)
            key_ingredients = []
            for item in keyword_list:
                if_in = is_in(item)
                if if_in != 'nothing':
                    if if_in not in key_ingredients:
                        key_ingredients.append(if_in)
                new_data[recipe_id]['ingredients'].append(item.replace(' ADVERTISEMENT', ''))

                c += 1
                if c == l - 1:
                    break
            new_data[recipe_id]['keywords'] = []
            for i in key_ingredients:
                new_data[recipe_id]['keywords'].append(i)
            parser.parser(new_data)
            complexity(new_data)
            new_data['seen'] = False
            new_data['like'] = False
    with open('recipe_data.json', 'w') as fp:
        json.dump(new_data, fp, sort_keys=True, indent=4, separators=(',', ': '))



def is_in(word):
    for i in keywords:
        if i in word:
            return i
    return 'nothing'


if __name__ == '__main__':
    add_keywords('keyword_file.txt', 'new_recipe_data.json')