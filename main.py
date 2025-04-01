from dataclasses import dataclass

@dataclass
class person:
    id:int
    m1:int
    m2:int
    m3:int

p0=person(1, 1, 0, 1)
print(p0)