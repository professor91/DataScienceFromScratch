# Data of Data Sciencester Network
users = [
    { "id": 0, "name": "Hero" },
    { "id": 1, "name": "Dunn" },
    { "id": 2, "name": "Sue" },
    { "id": 3, "name": "Chi" },
    { "id": 4, "name": "Thor" },
    { "id": 5, "name": "Clive" },
    { "id": 6, "name": "Hicks" },
    { "id": 7, "name": "Devin" },
    { "id": 8, "name": "Kate" },
    { "id": 9, "name": "Klein" }
]

# Friendship pairs among DS Network
# (0, 1) indicates 0 and 1 are friends
friendship_pairs = [(0, 1), (0, 2), (1, 2), (1, 3), (2, 3), (3, 4),
                    (4, 5), (5, 6), (5, 7), (6, 8), (7, 8), (8, 9)]

# Having friendship data as list of pairs is not the most efficient method,
# especially when we have large amounts of data so we will convert it into
# a dictionary

# Initialize a dict wtih an empty list for each user id
friendships= {user["id"]: [] for user in users}

# Abd loop over the friendship pairs to populate it
for i,j in friendship_pairs:
    friendships[i].append(j)
    friendships[j].append(i)

# What is the average number of connections?
def number_of_friends(user):
    """How many frineds does _user_ have?"""
    user_id= user["id"]
    friend_ids= friendships[user_id]
    return len(friend_ids)

total_connections = sum(number_of_friends(user) for user in users)  #24
num_users = len(users)

avg_connections = total_connections / num_users

# create a list (usre_id, number_of_friends)
num_frineds_by_id = [(user["id"], number_of_friends(user)) for user in users]


num_frineds_by_id.sort(         # sort the list
                        key = lambda id_and_friends: id_and_friends[1], # by num_friends
                        reverse=True)   # largest to smallest


# Data Sciencester You May Know
def foaf_ids_bad(user):
    return [foaf_id
            for friend_id in friendships[user["id"]]
            for foaf_id in friendships[friend_id]]


print(friendships[0])   # [1,2]
print(friendships[1])   # [0,2,3]
print(friendships[2])   # [0,1,3]

from collections import Counter

def friends_of_friends(user):
    user_id = user["id"]
    return Counter(
        foaf_id
        for friend_id in friendships[user_id]   # for each of my friends,
        for foaf_id in friendships[friend_id]   # find their friends
        if foaf_id != user_id                   # whi aren't me
        and foad_id not in friendships[user_id] # and aren't my friends
    )

    print(friends_of_friends(users[3]))         # Counter({0: 2,5: 1})