#/usr/bin/env python

class Vehicle():
    def __init__(self, name, color, engine):
        self.name = name
        self.color = color
        self.engine = engine

boeing = Vehicle("Tesla", "purple", "G800")
print(boeing.__str__())