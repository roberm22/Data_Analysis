# Import pandas package
import pandas as pd

df_marks = pd.DataFrame(s2, columns=['Student1'])
print("The dataframe created from series isn", df_marks)

# Create Height series (in feet)
height = pd.Series([5.3, 6.2, 5.8, 5.0, 5.5], index=['Person 1', 'Person 2', 'Person 3', 'Person 4', 'Person 5'])
# Create Weight Series (in kgs)
weight = pd.Series([65, 89, 75, 60, 59], index=['Person 1', 'Person 2', 'Person 3', 'Person 4', 'Person 5'])

# Create dataframe
df_person = pd.DataFrame({'height': height, 'weight': weight})
print("The Person table details are:n", df_person)

# Read data from .csv file
data = pd.read_csv('IMDB-Movie-Data.csv')

# Preview top 5 rows using head()
data.head()

data.info()

# Extract data as series
genre = data['Genre']

print(data.loc[['Suicide Squad']][['Genre', 'Actors', 'Director', 'Rating', 'Revenue (Millions)']])

print(data.iloc[10:15][['Title', 'Rating', 'Revenue (Millions)']])

print(data[((data['Year'] >= 2010) & (data['Year'] <= 2016))
           & (data['Rating'] < 6.0)
           & (data['Revenue (Millions)'] > data['Revenue (Millions)'].quantile(0.95))])

data.groupby('Director')[['Rating']].mean().head()
data.groupby('Director')[['Rating']].mean().sort_values(['Rating'], ascending=False).head()

# To check null values row-wise
data.isnull().sum()

# Use drop function to drop columns
data.drop('Metascore', axis=1).head()

# Drops all rows containing missing data
data.dropna()
# Drop all columns containing missing data
data.dropna(axis=1)
data.dropna(axis=0, thresh=6)

revenue_mean = data['Revenue (Millions)'].mean()
print("The mean revenue is: ", revenue_mean)


# Classify movies based on ratings
def rating_group(rating):
    if rating >= 7.5:
        return 'Good'
    elif rating >= 6.0:
        return 'Average'
    else:
        return 'Bad'

# Function on our movies data creating a new variable in the dataset to hold the rating category
data['Rating_category'] = data['Rating'].apply(rating_group)
