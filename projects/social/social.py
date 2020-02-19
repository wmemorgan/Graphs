import random
from util import Queue

class User:
    def __init__(self, name):
        self.name = name

class SocialGraph:
    def __init__(self):
        self.last_id = 0
        self.users = {}
        self.friendships = {}

    def add_friendship(self, user_id, friend_id):
        """
        Creates a bi-directional friendship
        """
        if user_id == friend_id:
            print("WARNING: You cannot be friends with yourself")
        elif friend_id in self.friendships[user_id] or user_id in self.friendships[friend_id]:
            print("WARNING: Friendship already exists")
        else:
            self.friendships[user_id].add(friend_id)
            self.friendships[friend_id].add(user_id)

    def add_user(self, name):
        """
        Create a new user with a sequential integer ID
        """
        self.last_id += 1  # automatically increment the ID to assign the new user
        self.users[self.last_id] = User(name)
        self.friendships[self.last_id] = set()

    def populate_graph(self, num_users, avg_friendships):
        """
        Takes a number of users and an average number of friendships
        as arguments

        Creates that number of users and a randomly distributed friendships
        between those users.

        The number of users must be greater than the average number of friendships.
        """
        # Reset graph
        self.last_id = 0
        self.users = {}
        self.friendships = {}

        # Add users
        for user in range(num_users):
            self.add_user(user)

        # Create friendships
        ## create a list with all possible friendships
        possible_friendships = []
        for user in range(1, self.last_id + 1):
            for friend in range(user + 1, self.last_id):
                possible_friendship = (user, friend)
                possible_friendships.append(possible_friendship)

        ## then shuffle it randomly
        random.shuffle(possible_friendships)
        ## and only take as many as we need,
        total_friendships = num_users * avg_friendships // 2
        random_friendships = possible_friendships[:total_friendships]
        ## and add those friendships
        for friendship in random_friendships:
            self.add_friendship(friendship[0], friendship[1])

    def get_all_social_paths(self, user_id):
        """
        Takes a user's user_id as an argument

        Returns a dictionary containing every user in that user's
        extended network with the shortest friendship path between them.

        The key is the friend's ID and the value is the path.
        """
        visited = {}  # Note that this is a dictionary, not a set
        # Implement BFT algorithm
        # make a queue
        queue = Queue()
        # add initial PATH to queue
        queue.enqueue([user_id])
        # loop through queue
        while queue.size() > 0:
            ## dequeue the path
            path = queue.dequeue()
            ## get current user
            current_user = path[-1]

            if current_user not in visited:
                visited[current_user] = path
                # iterate through friendships
                for friend in self.friendships[current_user]:
                    ## copy the path, add the neighbor to the
                    path_copy = list(path)
                    path_copy.append(friend)
                    ## for each one, add a PATH TO IT to our queue
                    queue.enqueue(path_copy)
                
        return visited


if __name__ == '__main__':
    sg = SocialGraph()
    sg.populate_graph(10, 2)
    print(f"friendships: {sg.friendships}")
    connections = sg.get_all_social_paths(1)
    print(f"connections: {connections}")
