class Members:
    def __init__(self, name, age, interests):
        self.name = name
        self.age = age
        self.interests = interests
        self.adjacent = {}

    def add_adjacent(self, vertex, weight = 0): #will be used later for relationship management
        self.adjacent[vertex] = weight

    def remove_adjacent(self, vertex): # AL YAMAN, remove adjacent
        if vertex in self.adjacent:
            del self.adjacent[vertex]

    def get_adjacent(self): # Abdullah get adjacent
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
    
    def add_adjacent(self, from_member, to_member, weight = 0): # AL YAMAN, add weighted adjacent
        self.members[from_member.name].add_adjacent(to_member.name, weight)
        if not self.directed: # creat adjacency for undirected graph
            self.members[to_member.name].add_adjacent(from_member.name, weight)
    
    def remove_adjacent(self, from_member, to_member): # Al yaman, remove adjacent
        self.members[from_member.name].remove_edge(to_member.name)
        if not self.directed:
            self.members[to_member.name].remove_edge(from_member.name)
    
    def get_member_friends(self, member):
        return self.members[member.name].get_adjacent()
    
    def find_mutual_friends(self, member1, member2): # Al yaman find mutual friends 
        member1_friends = set(self.members[member1.name].get_adjacent())
        member2_friends = set(self.members[member2.name].get_adjacent())
        mutual_friends = member1_friends.intersection(member2_friends)
        return mutual_friends

    def recommend_friends(self, member): # Al Yaman, recommend friends
        member_vertex = self.members[member.name]
        member_adjacent = set(member_vertex.get_adjacent())
        friend_recommendations = set() # Use a set to avoid duplicates
        for friend in member_adjacent:
            friend_vertex = self.members[friend]
            friend_adjacent = set(friend_vertex.get_adjacent())
            for friend_of_friend in friend_adjacent:
                if friend_of_friend == member.name:
                    continue
                if friend_of_friend in member_adjacent:
                    continue
                friend_recommendations.add(friend_of_friend) 
        return list(friend_recommendations) 
