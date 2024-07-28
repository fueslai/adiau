import pandas as pd

# Example DataFrame
data = {'A': ['foo', 'bar', 'foo', 'bar', 'foo'],
        'B': ['one', 'one', 'two', 'three', 'two'],
        'C': [1, 2, 3, 4, 5]}
df = pd.DataFrame(data)

# Selecting columns of type 'object' and describing them
object_summary = df.select_dtypes(include='object').describe()

print(object_summary)
