
class Members:# Abdullah, A members class (vertex)
    def __init__(self, name, age, interests):
        self.name = name
        self.age = age
        self.interests = interests
        self.adjacent = {}

    def add_adjacent(self, member, weight = 0): #Abdullah add adjacent
        self.adjacent[member] = weight

    def remove_adjacent(self, member): # AL YAMAN, remove adjacent
        if member in self.adjacent:
            del self.adjacent[member]

    def get_adjacent(self): # Abdullah, to see a member adjacent
        return list(self.adjacent.keys())

class Graph: #Abdullah, a graph class to represent the network
    def __init__(self, directed = False):
        self.members = {} # an empty
        self.directed = directed

    def add_member(self, member):# Abdullah,  method to add members
        if member.name not in self.members:
            self.members[member.name] = member
        else:
            print("member already exists")

    def remove_member(self, member): # Aydin, method to remove members
        if member.name in self.members:
            del self.members[member.name]
            for other_member in self.members.values(): #loops through the other members
                if member.name in other_member.adjacent:
                    del other_member.adjacent[member.name] #deletes the removed member from other members adjacent
        else:
            print("Member not found")
    
    def add_adjacent(self, from_member, to_member, weight = 0): # Al yaman, Add an edge between two members
        self.members[from_member.name].add_adjacent(to_member.name, weight)
        if not self.directed: # If undirected, add reverse edge
            self.members[to_member.name].add_adjacent(from_member.name, weight)
    
    def remove_adjacent(self, from_member, to_member): # Al yaman, Remove an edge between two members
        self.members[from_member.name].remove_adjacent(to_member.name)
        if not self.directed: # If undirected, remove reverse edge
            self.members[to_member.name].remove_adjacent(from_member.name)
    
    def get_member_friends(self, member): #Al yaman, Get all friends of a member
        return self.members[member.name].get_adjacent()
    
    def find_mutual_friends(self, member1, member2): # Aydin, Find mutual friends between two members
        member1_friends = set(self.members[member1.name].get_adjacent())
        member2_friends = set(self.members[member2.name].get_adjacent())
        mutual_friends = member1_friends.intersection(member2_friends)
        return mutual_friends

    def recommend_friends(self, member): # Aydin, Recommend friends based on mutual connections
        member_vertex = self.members[member.name]
        member_adjacent = set(member_vertex.get_adjacent())
        friend_recommendations = set() # Use a set to avoid duplicates
        for friend in member_adjacent: # Iterate through friends
            friend_vertex = self.members[friend]
            friend_adjacent = set(friend_vertex.get_adjacent())
            for friend_of_friend in friend_adjacent: # Check friends of friends
                if friend_of_friend == member.name:
                    continue
                if friend_of_friend in member_adjacent:
                    continue
                friend_recommendations.add(friend_of_friend) 
        return list(friend_recommendations)  # Return recommended friends

'''
# ----usage example----
graph = Graph()
p1 = Members("Abdullah", "19", "Volleyball, Video games")
p2 = Members("Abdullahi", "18", "Mountain Bikes, Cars")
p3 = Members("Hassan", "18", "Football, Rubics Cube")
p4 = Members("Aydin", "123", "Football, Coding")


graph.add_member(p1)
graph.add_member(p2)
graph.add_member(p3)
graph.add_member(p4)


graph.add_adjacent(p1, p2, 5)
graph.add_adjacent(p1, p3, 3)
graph.add_adjacent(p2, p3, 7)
graph.add_adjacent(p3, p4, 9)

print(graph.get_member_friends(p1))
graph.remove_adjacent(p1, p2)
print(graph.get_member_friends(p1))

print(graph.members.keys())
graph.remove_member(p1)
print(graph.members.keys())
'''