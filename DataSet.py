import pandas as pd
import numpy as np
# from Ingredients import Ingredient

class MyClass:
    
    def __init__(self, dataset):
        self.dataset = dataset
        for column in dataset.columns:
            setattr(self, column, dataset[column])
    
    # def greet(self):
    #     # print("Hello,", self.name)
    def print_dataset(self):
            print(self.dataset)
# Load the dataset from CSV
dataset = pd.read_csv('ingredients_finalised_dataset.csv')

# Instantiate the class with the dataset
# Instantiate the class with the dataset
obj = MyClass(dataset)
# objIngredient = Ingredient(None)
# Call the method to print the dataset
print(obj.StockQunatity)
# obj.print_dataset()