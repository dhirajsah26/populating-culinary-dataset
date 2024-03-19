import pandas as pd
import numpy as np
from DataSet import MyClass

class Ingredient:
    
    def __init__(self, dataset):
        self.dataset = dataset
        for column in dataset.columns:
            setattr(self, column, dataset[column])
    
    def print_dataset(self):
        print(self.dataset)

# Load the dataset from CSV
dataset = pd.read_csv('ingredient_presence_df.csv')

# Instantiate the class with the dataset
obj = Ingredient(dataset)

# Call the method to print the dataset
obj.print_dataset()



# Instantiate MyClass and print the dataset
obj = MyClass(None)  # Pass None since we're not using the dataset in this file
obj.print_dataset()