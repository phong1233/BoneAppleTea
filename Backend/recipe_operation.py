import json


def start_database():
    with open("original_recipe_data.json") as f:
        lines = f.readlines()
        lines = [l for l in lines]
        with open("recipe_data.json", "w") as f1:
            f1.writelines(lines)


def reset_like():
    open('recipe_like.json', 'w').close()
    open('recipe_dislike.json', 'w').close()


def send():
    with open('recipe_data.json', 'r') as f:
        data = json.load(f)
        to_send = {}
        to_send['recipe'] = []
        for i in range(len(data)):
            to_send['recipe'].append(data[str(i)])
            with open('recipe_data.json', 'r') as f1:
                file = json.load(f1)
                del file[str(i)]
            with open('recipe_data.json', 'a') as f1:
                json.dump(file, f1, sort_keys=False, indent=4, separators=(',', ': '))
        return to_send


def receive(dic):
    like = dic['like']
    id = dic['id']
    to_send = {id:dic}
    if like:
        with open('recipe_like.json', 'r') as f:
            try:
                file = json.load(f)
                file[str(id)] = dic
                with open('recipe_like.json', 'a') as f1:
                    json.dump(file, f1, sort_keys=False, indent=4, separators=(',', ': '))
            except:
                with open('recipe_like.json', 'a') as f1:
                    json.dump(to_send, f1, sort_keys=False, indent=4, separators=(',', ': '))
    else:
        '''with open('recipe_dislike.json', 'r') as f:
            try:
                file = json.load(f)
                file.update(dic)
                with open('recipe_dislike.json', 'a') as f1:
                    json.dump(file, f1, sort_keys=False, indent=4, separators=(',', ': '))
            except:
                with open('recipe_dislike.json', 'a') as f1:
                    json.dump(dic, f1, sort_keys=False, indent=4, separators=(',', ': '))'''
    with open('recipe_data.json', 'r') as f:
        file = json.load(f)
        del file[str(id)]

    with open('recipe_data.json', 'w') as f:
        json.dump(file, f, sort_keys=False, indent=4, separators=(',', ': '))

def reject(dic):
    with open('recipe_dislike.json', 'r') as f:
        try:
            file = json.load(f)
            file.update(dic)
            with open('recipe_dislike.json', 'a') as f1:
                json.dump(file, f1, sort_keys=False, indent=4, separators=(',', ': '))
        except:
            with open('recipe_dislike.json', 'a') as f1:
                json.dump(dic, f1, sort_keys=False, indent=4, separators=(',', ': '))

def accept():
    with open('recipe_like.json', 'r') as f:
        try:
            dic = request.json
            dic = json.load(dic)
            file = json.load(f)
            file.update(dic)
            with open('recipe_like.json', 'a') as f1:
                json.dump(file, f1, sort_keys=False, indent=4, separators=(',', ': '))
        except:
            with open('recipe_like.json', 'a') as f1:
                json.dump(dic, f1, sort_keys=False, indent=4, separators=(',', ': '))

start_database()