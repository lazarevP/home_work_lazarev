from .employee import Employee


class Recruiter(Employee):
    def work(self):
        work_rec = super(Recruiter, self).work()
        return work_rec[:-1] + 'start hiring'

    def __str__(self):
        return f'Recruiter: {self.name}'
