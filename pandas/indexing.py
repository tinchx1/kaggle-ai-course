import pandas as pd

data = pd.DataFrame({
    'A': [10, 20, 30],
    'B': [40, 50, 60]
}, index=['fila1', 'fila2', 'fila3'])

#loc (Label-based indexing - Indexación por etiquetas
print(data.loc['fila2'])  # Accede a la fila con índice 'fila2'
print(data.loc[['fila1', 'fila3'], 'B'])  # Accede a valores específicos


#iloc (Integer-based indexing - Indexación basada en enteros
print(data.iloc[1])  # Accede a la segunda fila (índice 1)
print(data.iloc[:, 0])  # Accede a la primera columna (índice 0)
print(data.iloc[0:2, 1])  # Accede a filas 0 y 1 de la columna 1

#In this case `df.iloc[0:1000]` will return 1000 entries, while `df.loc[0:1000]` return 1001 of them! To get 1000 elements using `loc`, you will need to go one lower and ask for `df.iloc[0:999]`. 

#groupby() created a group of reviews which allotted the same point values to the given wines. Then, for each of these groups, we grabbed the points() column and counted how many times it appeared. value_counts() is just a shortcut to this groupby() operation.

#df.groupby('column1')['column2'].value_counts()
#df.groupby('column1')['column2'].value_counts().unstack().fillna(0)