class Element:

    def scale_convertation(self, t, scale):

        if scale == 'K':
            temp = t - 273
        elif scale == 'F':
            temp = t * 9 / 5 + 32
        else:
            temp = t
        return temp

    def aggregation(self, t, scale):
        temp = self.scale_convertation(t, scale)
        if temp < self.t_m:
            print('it is solid')
        elif temp > self.t_m and temp < self.t_d:
            print('it is liquid')
        elif temp == self.t_m or temp == self.t_d:
            print('it is changing aggregation')
        else:
            print('it is gas')


class Iron(Element):
    t_m = 1538
    t_d = 2862


class Chlore(Element):
    t_m = -100
    t_d = -34


class Oxygen(Element):
    t_m = -218
    t_d = -182


t = int(input())
s = input()
iron_obj = Iron()
iron_obj.aggregation(t, s)

chlore_obj = Chlore()
chlore_obj.aggregation(t, s)

oxygen_obj = Oxygen()
oxygen_obj.aggregation(t, s)



