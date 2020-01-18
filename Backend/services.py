import json

class Services():
    def get_recipes(self):
        f = open("all_recipes.json", "r")
        text = f.read()
        json_acceptable_string = text.replace("'", "\"")
        d = json.loads(json_acceptable_string)
        temp = [] 
        count= 0
        for recipe in d['recipes']:
            if count == 10:
                break
            temp.append(recipe)
            count += 1
        for i in range(10):
            del d['recipes'][0]
        f = open("all_recipes.json", "w")
        f.write(json.dumps(d))
        return json.dumps(temp)