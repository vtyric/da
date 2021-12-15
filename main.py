import re
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


def get_percentile(salary):
    t = []
    for i in range(5, 105, 5):
        t.append(np.percentile(salary, i))
    return t


def make_plt(data, name):
    plt.plot(data, color="blue")
    plt.title(f'{name} с высшим образованием')
    plt.gca().axes.get_xaxis().set_visible(False)
    plt.show()


def make_gender_salary_graphic(gender_data, gender_name):
    data_without_nan = gender_data[gender_data["educationType"] == gender_data["educationType"]]
    higher_educated = data_without_nan[data_without_nan["educationType"].str.contains("Высшее")]
    middle_educated = data_without_nan[data_without_nan["educationType"].str.contains("Среднее")]

    make_plt(higher_educated["salary"][:300], gender_name)
    make_plt(middle_educated["salary"][:300], gender_name)


def print_data_to_file(data, data_name, filename):
    with open(filename, 'w', encoding='utf-8') as file:
        for d in data:
            print(d, file=file)
    print(f'{data_name} находятся в "{filename}"\n')


def main():
    data = pd.read_csv('works.csv', delimiter=',')
    print(f"Количество записей: {data.shape[0]}\n")
    men = data[data["gender"] == "Мужской"]
    women = data[data["gender"] == "Женский"]
    print(f"Количество мужчин: {men.shape[0]}")
    print(f"Количество женщин: {women.shape[0]}\n")
    not_nan_skills = data[data.skills == data.skills]
    print(f"не NAN в skills: {not_nan_skills.shape[0]}\n")
    skills = list(filter(lambda x: len(x) > 2,
                         map(lambda x: re.sub('<[^<]+?>', '', x).strip().split(','), not_nan_skills["skills"])))
    print_data_to_file(skills, "Заполненные скиллы", "skills.txt")
    python_specialists = not_nan_skills[not_nan_skills["skills"].str.contains("Python")]
    print_data_to_file(python_specialists["salary"], "Зарплата питон специалистов", "python_specialist_salary.txt")
    men_percentile = get_percentile(men["salary"])
    women_percentile = get_percentile(women["salary"])
    men_dispersion = np.std(men["salary"])
    women_dispersion = np.std(women["salary"])
    print(f"Перцентиль у мужчин с шагом 5 (5%, 10%, 15%,..., 100%):\n{men_percentile}")
    print(f"Разброс зарплаты у мужчин: {men_dispersion}\n")
    print(f"Перцентиль у женщин с шагом 5 (5%, 10%, 15%,..., 100%):\n{women_percentile}")
    print(f"Разброс зарплаты у женщин: {women_dispersion}\n")
    make_gender_salary_graphic(men, "мужчины")
    make_gender_salary_graphic(women, "женщины")


if __name__ == "__main__":
    main()
