class Person:
    people_count = 0

    @staticmethod
    def get_people_count():
        return Person.people_count

class Bob(Person):
    people_count = 2
    def __init__(self) -> None:
        super().__init__()

        print(self.get_people_count()) 

bob = Bob()

