from models import employee, programmer, recruiter, candidate, vacancy


def main():
    rec = recruiter.Recruiter('John', '0987654321', 400)
    dev1 = programmer.Programmer('Bob', '0987654322', 350)
    dev2 = programmer.Programmer('Bill', '0987654333', 450)
    can1 = candidate.Candidate('Jack Daniel', 'jack228@hotmail.com', '', '', '')


if __name__ == '__main__':
    main()


