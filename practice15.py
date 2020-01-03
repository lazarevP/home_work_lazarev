from datetime import date, datetime, timedelta


class Employee:

    def __init__(self, name, phone, salary_per_day):
        self.name = name
        self.phone = phone
        self.salary_per_day = salary_per_day

    def __lt__(self, other):
        return self.salary_per_day < other.salary_per_day

    def __gt__(self, other):
        return self.salary_per_day > other.salary_per_day

    def __eq__(self, other):
        return self.salary_per_day == other.salary_per_day

    def __le__(self, other):
        return self.salary_per_day <= other.salary_per_day

    def __ge__(self, other):
        return self.salary_per_day >= other.salary_per_day

    def __neg__(self, other):
        return self.salary_per_day != other.salary_per_day

    def work(self):
        return "I come to the office."

    def check_salary(self, days):
        return days * self.salary_per_day

    def now_selery(self):
        now = date.today()
        month_start = date(now.year, now.month, 1)

        weekend = [5, 6]

        diff = (now - month_start).days + 1

        day_count = 0

        for day in range(diff):
            result = (month_start + timedelta(day)).weekday()
            if (month_start + timedelta(day)).weekday() not in weekend:
                day_count += 1

            print(day_count)


class Recruiter(Employee):
    def work(self):
        work_rec = super(Recruiter, self).work()
        return work_rec[:-1] + 'start hiring'

    def __str__(self):
        return 'Recruiter: {}'.format(self.name)


class Programmer(Employee):
    def work(self):
        return super(Programmer, self).work()[:-1] + 'start coding'

    def __str__(self):
        return 'Programmer: {}'.format(self.name)







