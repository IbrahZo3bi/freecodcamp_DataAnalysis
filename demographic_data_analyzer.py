import pandas as pd

def max_percentage(df):
    max=round(100*len(df.loc[(df['salary']=='>50K')&(df['native-country']=='United-States')])/len(df.loc[df['native-country']=='United-States']),1)
    max_c='United-States'
    for country in df['native-country'].unique():
    
    max_p=round(100*len(df.loc[(df['salary']=='>50K')&(df['native-country']==country)])/len(df.loc[df['native-country']==country]),1)
    if max_p>max:
        max=max_p
        max_c=country
    return max_c,max_p


def calculate_demographic_data(print_data=True):
    # Read data from file
    df = pd.read_csv(r"/workspace/boilerplate-demographic-data-analyzer/demographic_data_analyzer.py")

    # How many of each race are represented in this dataset? This should be a Pandas series with race names as the index labels.
    race_count = df['race'].value_counts()

    # What is the average age of men?
    average_age_men = round( df.groupby('sex')['age'].mean()['Male'], 1 )

    # What is the percentage of people who have a Bachelor's degree?
    percentage_bachelors = round((df.loc[df['education']=='Bachelors'].value_counts().sum()/df.value_counts().sum())*100,1)

    # What percentage of people with advanced education (`Bachelors`, `Masters`, or `Doctorate`) make more than 50K?
    # What percentage of people without advanced education make more than 50K?



    # with and without `Bachelors`, `Masters`, or `Doctorate`
    higher_education = df.loc[((df['education']=='Bachelors') | (df['education']=='Masters')|(df['education']=='Doctorate'))]
    lower_education = df.loc[(~(df['education']=='Bachelors') | (df['education']=='Masters')|(df['education']=='Doctorate'))]

    # percentage with salary >50K
    higher_education_rich = round((higher_education['salary']=='>50k').sum()/len(higher_education)*100,1)
    lower_education_rich = round((lower_education['salary']=='>50K').sum()/len(lower_education)*100,1)


    # What is the minimum number of hours a person works per week (hours-per-week feature)?
    min_work_hours = df['hours-per-week'].min()

    # What percentage of the people who work the minimum number of hours per week have a salary of >50K?
    num_min_workers = len(df.loc[(df['hours-per-week']==df['hours-per-week'].min())])

    rich_percentage = round(100*(len(df.loc[(df['hours-per-week']==df['hours-per-week'].min()&(df['salary']=='>50K'))])/num_min_workers),1)

    # What country has the highest percentage of people that earn >50K?
    
    highest_earning_country,highest_earning_country_percentage=max_percentage(df)

    # Identify the most popular occupation for those who earn >50K in India.
    ind=df.loc[(df['native-country']=='India')&(df['salary']=='>50K')]
    
    top_IN_occupation = ind['occupation'].value_counts().keys()[0]

    # DO NOT MODIFY BELOW THIS LINE

    if print_data:
        print("Number of each race:\n", race_count) 
        print("Average age of men:", average_age_men)
        print(f"Percentage with Bachelors degrees: {percentage_bachelors}%")
        print(f"Percentage with higher education that earn >50K: {higher_education_rich}%")
        print(f"Percentage without higher education that earn >50K: {lower_education_rich}%")
        print(f"Min work time: {min_work_hours} hours/week")
        print(f"Percentage of rich among those who work fewest hours: {rich_percentage}%")
        print("Country with highest percentage of rich:", highest_earning_country)
        print(f"Highest percentage of rich people in country: {highest_earning_country_percentage}%")
        print("Top occupations in India:", top_IN_occupation)

    return {
        'race_count': race_count,
        'average_age_men': average_age_men,
        'percentage_bachelors': percentage_bachelors,
        'higher_education_rich': higher_education_rich,
        'lower_education_rich': lower_education_rich,
        'min_work_hours': min_work_hours,
        'rich_percentage': rich_percentage,
        'highest_earning_country': highest_earning_country,
        'highest_earning_country_percentage':
        highest_earning_country_percentage,
        'top_IN_occupation': top_IN_occupation
    }
