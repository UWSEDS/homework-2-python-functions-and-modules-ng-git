import pandas as pd
import requests

# read CSV file
def read(url, filename):
    r = requests.get(url, allow_redirects=True)
    open(filename, 'wb').write(r.content)
    df = pd.read_csv(filename)
    return df

def test_create_dataframe(df,columnList):
    # count the row amounts
    count = 0
    for i in list(df.columns):
        count = count + 1
    row = df.size//count
    if row < 10:
        return False
    
    # check the column types
    for i in range(count):
        if df.dtypes[i] != df.dtypes[0]:
            return False
   
    # check if the DataFrame contains only the columns that you specified as the second argument
    set2 = set(columnList)
    set1 = set(list(df.columns))
    return set1.issubset(set2)

    
