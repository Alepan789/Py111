"""
class Glass:
    def __init__(self, name, volume):
        self.name = name
        self.volume = volume

g = Glass('Мая стакан', 550)
g2 = Glass('твой стакан', 330)
print(g.name, g.volume, g.__dict__)
g.__dict__["volume"] = 777
print(g.__dict__)
print(hasattr(g,'name'))

print('has:',hasattr(g,'__bool__'))
print(bool(g))
"""
a = '01:15'
print(a.split(':'))

def