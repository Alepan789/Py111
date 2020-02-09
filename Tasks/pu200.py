
class Glass:
    def __init__(self):
        print(hex(id(self)))
        self.capacity_volume = 500
        self.occupied_volume = 0
    def add_water(self, water):
        empty_volume = self.capacity_volume - self.occupied_volume
        remaning_liquid = 0
        if water > empty_volume:
            remaning_liquid = water - empty_volume
            self.occupied_volume = water - remaning_liquid
            return remaning_liquid

    def __str__(self):
        return f'Capacity: {self.capacity_volume}\nCurrent: {self.occupied_volume}'

# glass1 = Glass()
# glass2 = Glass()
# glass3 = Glass()
# print(a, type(a), isinstance(a, int), dir(Glass))
print('Glass 1')
glass1 = Glass()
print(hex(id(glass1)))
print('Glass 2')
glass2 = Glass()
print(hex(id(glass2)))
print('Glass 3')
glass3 = Glass()
print(hex(id(glass3)))
print(glass3)
# print(dir(Glass))
# print(glass1() in glass2())