import json


def send_next_10():
    with open('recipe_data.json', 'r') as f:
        data = json.load(f)
        to_send = {}
        to_send['recipe'] = []
        for i in range(10):
            to_send['recipe'].append(data[str(i)])
        print(to_send)
        return to_send
