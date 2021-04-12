import pandas as pd

data = "https://bites-data.s3.us-east-2.amazonaws.com/summer.csv"


def athletes_most_medals(data=data):
    df = pd.read_csv(data)
    
    top_man = df.groupby('Gender')['Athlete'].value_counts()['Men'].idxmax()
    top_woman = df.groupby('Gender')['Athlete'].value_counts()['Women'].idxmax()
    
    medal_counts = df['Athlete'].value_counts()
    
    results_dict = {'Names': [top_man, top_woman], 'Medals': [medal_counts[top_man], medal_counts[top_woman]]}
    
    return pd.DataFrame(results_dict['Medals'], index=results_dict['Names'], columns=['Medals'])
    pass

