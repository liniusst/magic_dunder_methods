# pylint: disable= missing-docstring
# __str__
# __repr__
# __len__
# __bool__
# __getitem__


class Visitor:
    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        self.visitors = []

    def __str__(self) -> str:
        return f"Person {self.name} is {self.age} years old"

    def __repr__(self) -> str:
        return f"CheckSystem({self.name}, {self.age})."

    def __len__(self) -> int:
        return len(self.visitors)

    def __bool__(self) -> bool:
        if self.age >= 18:
            return True
        else:
            return False

    def __eq__(self, other: "Visitor") -> bool:
        if isinstance(other, Visitor):
            return self.name == other.name and self.age == other.age
        return False


class VisitorData:
    def __init__(self, visitor_info: Visitor) -> None:
        self.visitor_info = visitor_info
        self.visitor_data = {"Name": [], "Age": [], "Adult": []}

    def __getitem__(self, key: str):
        return self.visitor_data[key]

    def __eq__(self, other: "VisitorData") -> bool:
        if isinstance(other, VisitorData):
            return (
                self.visitor_info.name == other.visitor_info.name
                and self.visitor_info.age == other.visitor_info.age
            )
        return False

    def add_visitor_data(self):
        self.visitor_data["Name"].append(self.visitor_info.name)
        self.visitor_data["Age"].append(self.visitor_info.age)
        self.visitor_data["Adult"].append(bool(self.visitor_info))
        return self.visitor_data

    def get_visitor_data(self):
        return self.visitor_data


person = Visitor(name="Linas", age=18)
person2 = Visitor(name="Antanas", age=20)
person3 = Visitor(name="Linas", age=18)
print(person == person2)  # 1
print(bool(person))  # 2
print(str(person))  # 3
print(repr(person))  # 4
person.visitors.append(person.name)
print(len(person))  # 5

info = VisitorData(visitor_info=person)
info.add_visitor_data()
visitor_dict = info.get_visitor_data()
print(visitor_dict)
print(visitor_dict["Name"])  # 6
