class Members:
    def __init__(self, name, age, interests):
        self.name = name
        self.age = age
        self.interests = interests
        self.adjacent = {}

    def add_adjacent(self, vertex, weight = 0): #will be used later for relationship management
        self.adjacent[vertex] = weight

    def get_adjacent(self, vertex):
        return list(self.adjacent.keys())

class Graph:
    def __init__(self, directed = False):
        self.members = {}
        self.directed = directed

    def add_member(self, member):
        if member not in self.members:
            self.members[member.name] = member
        else:
            print("member already exists")

    def remove_member(self, member):
        if member.name in self.members:
            del self.members[member.name]

            for other_member in self.members.values():
                if member.name in other_member.adjacent:
                    del other_member.adjacent[member.name]

        else:
            print("Member not found")