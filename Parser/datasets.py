import requests, bs4, sys, webbrowser
import json

keywords = ['chicken', 'onion', 'pot roast', 'egg', 'ginger', 'chocolate', 'pasta', 'garlic', 'milk', 'walnut', 'banana', 'potato', 'spinach', 'lemon', 'cod', 'zucchini', 'egg', 'oyster', 'fish', 'crabs', 'pumpkin', 'beef', 'carrot', 'blueberries', 'cheese', 'tomato', 'noodles', 'honey', 'ham', 'celery', 'pea', 'apple', 'cabbage', 'maple syrupt', 'graham crackers', 'pepper', 'avocado', 'chili beans', 'corn', 'cornmeal', 'spaghetti', 'cocoa', 'salmon', 'tuna', 'lamb', 'mushroom', 'cinnamon', 'quinoa', 'raspberries', 'strawberries', 'pork']


def get_url(item):
    address = requests.get('https://www.allrecipes.com/search/results/'+item)
    address.raise_for_status()
    soup = bs4.=(address.text, features="html.parser")
    recList = soup.find('ar-save-item')['data-imageurl']
    recipe = recList[1:]
    recipe = recipe[:-1]
    print(recipe)
    return recipe


def parse_json():
    new_data = {}
    count = 100
    with open('recipes_raw_nosource_ar.json') as json_file:
        data = json.load(json_file)
        recipe_id = 0
        for d in data:
            print(d)
            new_data[recipe_id] = data[d]
            new_data[data[d]['title']]['picture_link'] = get_url(data[d]['title'])
            ingredients = new_data[data[d]['title']]['ingredients']
            new_data[data[d]['title']]['ingredients'] = []
            c = 0
            l = len(ingredients)
            key_ingredients = []
            for item in ingredients:
                if_in = is_in(item)
                if if_in != 'nothing':
                    if if_in not in key_ingredients:
                        key_ingredients.append(if_in)
                new_data[data[d]['title']]['ingredients'].append(item.replace(' ADVERTISEMENT', ''))
                c += 1
                if c == l - 1:
                    break
            new_data[data[d]['title']]['keywords'] = []
            for i in key_ingredients:
                new_data[data[d]['title']]['keywords'].append(i)

            if count == 0:
                break
            count -= 1
            recipe_id += 1

    with open('new_recipe_data.json', 'w') as fp:
        json.dump(new_data, fp, sort_keys=True, indent=4, separators=(',', ': '))

def is_in(word):
    for i in keywords:
        if i in word:
            return i
    return 'nothing'

if __name__ == '__main__':
    parse_json()
    #create_dic()