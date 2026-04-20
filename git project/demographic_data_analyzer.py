import pandas as pd

def calculate_demographic_data(print_data=True):
    # Load dataset
    df = pd.read_csv("adult.data.csv")  # Replace with your CSV file

    # 1. How many of each race?
    race_count = df['race'].value_counts()

    # 2. Average age of men
    average_age_men = round(df[df['sex'] == 'Male']['age'].mean(), 1)

    # 3. Percentage with Bachelors
    percentage_bachelors = round((df['education'] == 'Bachelors').mean() * 100, 1)

    # 4. Percentage with advanced education (>50K)
    higher_education = df['education'].isin(['Bachelors', 'Masters', 'Doctorate'])
    lower_education = ~higher_education

    higher_edu_rich = df[higher_education & (df['salary'] == '>50K')].shape[0]
    higher_edu_total = df[higher_education].shape[0]
    percentage_higher_edu_rich = round(higher_edu_rich / higher_edu_total * 100, 1)

    lower_edu_rich = df[lower_education & (df['salary'] == '>50K')].shape[0]
    lower_edu_total = df[lower_education].shape[0]
    percentage_lower_edu_rich = round(lower_edu_rich / lower_edu_total * 100, 1)

    # 5. Minimum hours per week
    min_work_hours = df['hours-per-week'].min()

    # 6. % of rich among min hour workers
    min_workers = df[df['hours-per-week'] == min_work_hours]
    rich_min_workers = round((min_workers['salary'] == '>50K').mean() * 100, 1)

    # 7. Country with highest % of >50K earners
    country_rich = df[df['salary'] == '>50K']['native-country'].value_counts()
    country_total = df['native-country'].value_counts()
    highest_earning_country_percentage = round((country_rich / country_total * 100).max(), 1)
    highest_earning_country = (country_rich / country_total * 100).idxmax()

    # 8. Most popular occupation for rich in India
    india_rich = df[(df['native-country'] == 'India') & (df['salary'] == '>50K')]
    top_IN_occupation = india_rich['occupation'].value_counts().idxmax() if not india_rich.empty else None

    if print_data:
        print("Number of each race:\n", race_count)
        print("Average age of men:", average_age_men)
        print("Percentage with Bachelors:", percentage_bachelors)
        print("Percentage with higher education that earn >50K:", percentage_higher_edu_rich)
        print("Percentage without higher education that earn >50K:", percentage_lower_edu_rich)
        print("Minimum work hours per week:", min_work_hours)
        print("Percentage of rich among those who work fewest hours:", rich_min_workers)
        print("Country with highest % of rich:", highest_earning_country)
        print("Highest % of rich people in country:", highest_earning_country_percentage)
        print("Top occupation in India for those earning >50K:", top_IN_occupation)

    return {
        'race_count': race_count,
        'average_age_men': average_age_men,
        'percentage_bachelors': percentage_bachelors,
        'percentage_higher_edu_rich': percentage_higher_edu_rich,
        'percentage_lower_edu_rich': percentage_lower_edu_rich,
        'min_work_hours': min_work_hours,
        'rich_min_workers': rich_min_workers,
        'highest_earning_country': highest_earning_country,
        'highest_earning_country_percentage': highest_earning_country_percentage,
        'top_IN_occupation': top_IN_occupation
    }

# Run the function
if __name__ == "__main__":
    calculate_demographic_data()