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
    def __init__(self,t_m, t_d):
        self.t_m = t_m
        self.t_d = t_d

temperature = int(input())
shkala = input()

material = Element(temperature, shkala)