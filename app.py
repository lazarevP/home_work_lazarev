from models import employee, programmer, recruiter, candidate, vacancy


def main():
    rec = recruiter.Recruiter('John', '0987654321', 400)
    dev1 = programmer.Programmer('Bob', '0987654322', 350)
    dev2 = programmer.Programmer('Bill', '0987654333', 450)
    can1 = candidate.Candidate('Jack Daniel', 'jack228@hotmail.com', '?', '?', '?')
    can2 = candidate.Candidate('Ivan', 'vanya@gmail.com', '?', '?', '?')
    can3 = candidate.Candidate('Roma', 'user@mail.ru', '?', '?', '?')
    vac1 = vacancy.Vacancy('python developer', 'Django', 'middle')
    vac2 = vacancy.Vacancy('js developer', 'JQuery', 'middle')


if __name__ == '__main__':
    main()


def validate(list_of_all_emails):
    new_list = []
    for email in list_of_all_emails:
        if email not in new_list:
            new_list.append(email)
    if len(new_list) < len(list_of_all_emails):
        raise ValueError

