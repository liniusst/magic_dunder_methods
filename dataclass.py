from dataclasses import dataclass


# class Position:
#     def __init__(self, name: str, lan: float, leng: float) -> None:
#         self.name = name
#         self.lan = lan
#         self.leng = leng


@dataclass
class Position:
    name: str
    lan: float
    long: float


pos = Position(name="Vilnius", lan=0.1, long=0.0)
print(pos.name, pos.lan, pos.long)
