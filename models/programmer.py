from .employee import Employee


class Programmer(Employee):
    def work(self):
        return super(Programmer, self).work()[:-1] + 'start coding'

    def __str__(self):
        return 'Programmer: {}'.format(self.name)
