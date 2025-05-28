import pandas as pd

def demographic_data_analysis():
    # Load dataset with headers
    df = pd.read_csv("adult.data", header=None, names=[
        "age", "workclass", "fnlwgt", "education", "education-num", "marital-status",
        "occupation", "relationship", "race", "sex", "capital-gain", "capital-loss",
        "hours-per-week", "native-country", "salary"
    ])

    # Strip whitespace from string columns (fix applymap warning)
    for col in df.select_dtypes(include=['object']).columns:
        df[col] = df[col].str.strip()

    # 1. How many people of each race
    race_count = df['race'].value_counts()

    # 2. Average age of men
    average_age_men = round(df[df['sex'] == 'Male']['age'].mean(), 1)

    # 3. Percentage of people who have a Bachelor's degree
    percentage_bachelors = round(
        (df['education'] == 'Bachelors').mean() * 100, 1)

    # 4 & 5. Advanced education and income >50K
    higher_education = df['education'].isin(['Bachelors', 'Masters', 'Doctorate'])
    higher_education_rich = round(
        (df[higher_education]['salary'] == '>50K').mean() * 100, 1)

    lower_education_rich = round(
        (df[~higher_education]['salary'] == '>50K').mean() * 100, 1)

    # 6. Minimum number of hours worked per week
    min_work_hours = df['hours-per-week'].min()

    # 7. Percentage of rich among those who work minimum hours
    num_min_workers = df[df['hours-per-week'] == min_work_hours]
    rich_percentage_min_workers = round(
        (num_min_workers['salary'] == '>50K').mean() * 100, 1)

    # 8. Country with highest percentage of people earning >50K
    country_counts = df['native-country'].value_counts()
    country_rich_counts = df[df['salary'] == '>50K']['native-country'].value_counts()

    rich_percentage_by_country = (country_rich_counts / country_counts * 100).dropna()
    highest_earning_country = rich_percentage_by_country.idxmax()
    highest_earning_country_percentage = round(rich_percentage_by_country.max(), 1)

    # 9. Most popular occupation for those who earn >50K in India
    top_IN_occupation = df[(df['native-country'] == 'India') & (df['salary'] == '>50K')]['occupation'].mode()
    top_IN_occupation = top_IN_occupation.iloc[0] if not top_IN_occupation.empty else None

    # Prepare results dictionary
    results = {
        "race_count": race_count,
        "average_age_men": average_age_men,
        "percentage_bachelors": percentage_bachelors,
        "percentage_higher_education_rich": higher_education_rich,
        "percentage_lower_education_rich": lower_education_rich,
        "min_work_hours": min_work_hours,
        "rich_percentage_min_workers": rich_percentage_min_workers,
        "highest_earning_country": highest_earning_country,
        "highest_earning_country_percentage": highest_earning_country_percentage,
        "top_IN_occupation": top_IN_occupation
    }

    # Print results
    print("Number of each race:\n", race_count)
    print("Average age of men:", average_age_men)
    print("Percentage with Bachelors degrees:", percentage_bachelors)
    print("Percentage with higher education that earn >50K:", higher_education_rich)
    print("Percentage without higher education that earn >50K:", lower_education_rich)
    print("Min work time:", min_work_hours, "hours/week")
    print("Percentage of rich among those who work fewest hours:", rich_percentage_min_workers)
    print("Country with highest percentage of rich:", highest_earning_country)
    print("Highest percentage of rich people in country:", highest_earning_country_percentage)
    print("Top occupations in India for those who earn >50K:", top_IN_occupation)

    return results

# If you want to run the script directly
if __name__ == "__main__":
    demographic_data_analysis()



