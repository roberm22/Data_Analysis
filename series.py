# Import pandas package
import pandas as pd

s1 = pd.Series([10, 20, 30, 40, 50])
print("The series values are:", s1.values)
print("The index values are:", s1.index.values)

s2 = pd.Series([80, 93, 78, 85, 97], index=['English', 'Science', 'Social', 'Tamil', 'Maths'])
print("The Marks obtained by student are", s2)

# slicing using default integer index
print(s1[1:4])

dict_fruits = {'Orange': 80,
               'Apples': 210,
               'Bananas': 50,
               'Grapes': 90,
               'Watermelon': 70}

# Convert this dictionary into a series
fruits = pd.Series(dict_fruits)
print("Fruits and prices", fruits)

# Slice the series and retrieve price of Grapes
print("The price per kg of grapes is:", fruits['Grapes'])


