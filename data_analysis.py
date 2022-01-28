import pandas as pd

students = [{
    "name": "Jorge",
    "surname": "Perez",
    "age": 24,
    "weight": 50,
    "height": 170
}, {
    "name": "Pepe",
    "surname": "Garcia",
    "age": 27,
    "weight": 60,
    "height": 175
},
    {
        "name": "Aria",
        "surname": "Jimenez",
        "age": 26,
        "weight": 70,
        "height": 180
    },
    {
        "name": "Maria",
        "surname": "Ruz",
        "age": 25,
        "weight": 75,
        "height": 181
    },
    {
        "name": "Luisa",
        "surname": "Perez",
        "age": 24,
        "weight": 50,
        "height": 170
    },
    {
        "name": "Luisa",
        "surname": "Perez",
        "age": 24,
        "weight": 50,
        "height": 170
    }]

df = pd.DataFrame(students)

""" Resultados """
# df.head()

""" Información estadística básica"""
print(df.shape)
df.info()
df.describe()

print(df.columns)  # Devuelve una lista con los nombres de las columnas
print(df.name)  # Devuelve la serie llamada Name
print(df['name'])  # Otra forma de llamar a la serie Name
print(df[['name', 'surname']])  # Devuelve las series Name y Surname

""" Rename """
nombres = {
    'Name': 'Nombre',
    'Surname': 'Apellido'
}
df = df.rename(columns=nombres)

df.nombre.value_counts()  # Devuelve los diferentes nombres y el número de registros que hay para cada uno de ellos
df.nombre.unique()
