import pandas as pd

def calculate_demographic_data(print_data=True):
    # Read data
    df = pd.read_csv("adult.data.csv")

    # 1. Race count
    race_count = df['race'].value_counts()

    # 2. Average age of men
    average_age_men = round(df[df['sex'] == 'Male']['age'].mean(), 1)

    # 3. Percentage with Bachelor's degree
    total_people = len(df)
    bachelors = df[df['education'] == 'Bachelors']
    percentage_bachelors = round((len(bachelors) / total_people) * 100, 1)

    # 4. Advanced education >50K
    higher_edu = df[df['education'].isin(['Bachelors', 'Masters', 'Doctorate'])]
    higher_edu_rich = higher_edu[higher_edu['salary'] == '>50K']
    higher_education_rich = round((len(higher_edu_rich) / len(higher_edu)) * 100, 1)

    # 5. Without advanced education >50K
    lower_edu = df[~df['education'].isin(['Bachelors', 'Masters', 'Doctorate'])]
    lower_edu_rich = lower_edu[lower_edu['salary'] == '>50K']
    lower_education_rich = round((len(lower_edu_rich) / len(lower_edu)) * 100, 1)

    # 6. Min work hours
    min_work_hours = df['hours-per-week'].min()

    # 7. % rich among those who work min hours
    min_workers = df[df['hours-per-week'] == min_work_hours]
    rich_min_workers = min_workers[min_workers['salary'] == '>50K']
    rich_percentage = round((len(rich_min_workers) / len(min_workers)) * 100, 1)

    # 8. Country with highest % >50K
    country_group = df.groupby('native-country')
    country_percent = (country_group.apply(
        lambda x: (x['salary'] == '>50K').sum() / len(x) * 100
    ))

    highest_earning_country = country_percent.idxmax()
    highest_earning_country_percentage = round(country_percent.max(), 1)

    # 9. Top occupation in India (>50K)
    india = df[(df['native-country'] == 'India') & (df['salary'] == '>50K')]
    top_IN_occupation = india['occupation'].value_counts().idxmax()

    # Print results
    if print_data:
        print("Race Count:\n", race_count)
        print("Average age of men:", average_age_men)
        print("Percentage with Bachelors:", percentage_bachelors)
        print("Higher education >50K:", higher_education_rich)
        print("Lower education >50K:", lower_education_rich)
        print("Min work hours:", min_work_hours)
        print("Rich % among min workers:", rich_percentage)
        print("Highest earning country:", highest_earning_country)
        print("Highest earning country %:", highest_earning_country_percentage)
        print("Top occupation in India:", top_IN_occupation)

    return {
        'race_count': race_count,
        'average_age_men': average_age_men,
        'percentage_bachelors': percentage_bachelors,
        'higher_education_rich': higher_education_rich,
        'lower_education_rich': lower_education_rich,
        'min_work_hours': min_work_hours,
        'rich_percentage': rich_percentage,
        'highest_earning_country': highest_earning_country,
        'highest_earning_country_percentage': highest_earning_country_percentage,
        'top_IN_occupation': top_IN_occupation
    }