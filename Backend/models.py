class Recipe():
    def __init__(self, dic):
        self.name = dic['name']
        self.instructions = dic['instructions']
        self.ingredients = dic['ingredients']
        self.image = dic['image']
        self.keywords = dic['keywords']
        self.complexity = dic['complexity']
