import json


def start_database():
    with open("original_recipe_data.json") as f:
        lines = f.readlines()
        lines = [l for l in lines]
        with open("recipe_data.json", "w") as f1:
            f1.writelines(lines)


def reset_like():
    open('recipe_like.json', 'w').close()
    open('recipe_unlike.json', 'w').close()


def send_next_10():
    with open('original_recipe_data.json', 'r') as f:
        data = json.load(f)
        to_send = {}
        to_send['recipe'] = []
        for i in range(len(data)):
            to_send['recipe'].append(data[str(i)])

        with open('recipe_like.json', 'w') as f:
            json.dump(to_send, f, indent=4, separators=(',', ': '))

def receive(dic):
    like = list(dic.values())[0]['like']
    id = list(dic.values())[0]['id']
    if like:
        with open('recipe_like.json', 'r') as f:
            try:
                file = json.load(f)
                file.update(dic)
                with open('recipe_like.json', 'a') as f:
                    json.dump(file, f)
            except:
                pass
    else:
        with open('recipe_dislike.json', 'r') as f:
            try:
                file = json.load(f)
                file.update(dic)
                with open('recipe_dislike.json', 'a') as f:
                    json.dump(file, f)
            except:
                pass
    with open('recipe_data.json', 'r') as f:
        file = json.load(f)
        del file[str(id)]
    with open('recipe_data.json', 'a') as f:
        json.dump(file, f)

dic = {
    "0": {
        "ingredients": [
            "4 skinless, boneless chicken breast halves",
            "2 tablespoons butter",
            "2 (10.75 ounce) cans condensed cream of chicken soup",
            "1 onion, finely diced",
            "2 (10 ounce) packages refrigerated biscuit dough, torn into pieces"
        ],
        "instructions": [
            "Place the chicken, butter, soup, and onion in a slow cooker, and fill with enough water to cover.",
            "Cover, and cook for 5 to 6 hours on High. About 30 minutes before serving, place the torn biscuit dough in the slow cooker. Cook until the dough is no longer raw in the center."
        ],
        "picture_link": "https://images.media-allrecipes.com/userphotos/300x300/806223.jpg",
        "title": "Slow Cooker Chicken and Dumplings",
        "keywords": [
            "chicken",
            "onion",
            "chicken soup",
            "biscuit dough",
            "butter",
            "cream"
        ],
        "complexity": 1,
        "seen": False,
        "like": False,
        "id": 0,
        "similar_recipes": [
            "763",
            "403",
            "554",
            "886",
            "4"
        ]
    }}
send_next_10()