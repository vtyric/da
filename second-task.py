import pandas as pd


def count_people_diploma_not_match_job(data):
    result = 0
    for (jt, q) in zip(data["jobTitle"], data["qualification"]):
        if not does_diploma_match(jt, q) and not does_diploma_match(q, jt):
            result += 1
    return result


def get_top_job(data, job, first_parameter, second_parameter):
    workers = data[data[first_parameter].str.contains(job)]
    return workers[second_parameter].value_counts().head(5)


def does_diploma_match(first, second):
    words = first.lower().replace('-', ' ').split()
    for word in words:
        if word in second.lower():
            return True
    return False


def main():
    works = pd.read_csv("works.csv").dropna()
    works = works.apply(lambda record: record.astype(str).str.lower())
    number_of_people = count_people_diploma_not_match_job(works)
    print(f"Из {works.shape[0]} людей не совпадают профессия и должность у {number_of_people}")

    print("\nТоп образований людей, которые работают менеджерами:")
    print(get_top_job(works, "менеджер", "jobTitle", "qualification"))

    print("\nТоп должностей людей, которые по диплому являются инженерами:")
    print(get_top_job(works, "инженер", "qualification", "jobTitle"))


if __name__ == '__main__':
    main()
