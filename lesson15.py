from datetime import date, datetime, timedelta

class Employee:
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name

    @staticmethod
    def now_salery():
        now = date.today()
        month_start = date(now.year, now.month, 1)

        weekend = [5, 6]

        diff = (now - month_start).days + 1

        day_count = 0

        for day in range(diff):
            result = (month_start + timedelta(day)).weekday()
            if (month_start + timedelta(day)).weekday() not in weekend:
                day_count += 1

            return day_count

    @property
    def __str__(self):
        return f"{self.__class__.__name__}, {self.first_name}, {self.last_name}, {self.now_salery()}"

    @classmethod
    def candidate_creator(cls):
        file = open('candidates.csv', 'w')
        file.split(',')
        return 



