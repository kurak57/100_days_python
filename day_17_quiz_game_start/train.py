class User:
    def __init__(self,user_id, username):
        self.id = user_id
        self.username = username
        self.followers = 0
        self.following = 0

    def follow(self, user):
        user.followers += 1
        self.following += 1

user_1 = User("001","Tomi")
user_2 = User("002", "Queen")

user_1.follow(user_2)

print(
   f'''
username: {user_1.username}
following: {user_1.following}
followers: {user_1.followers}
'''
)