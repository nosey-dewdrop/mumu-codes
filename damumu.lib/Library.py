from User import User

class Library:
    
      def __init__(self):
            self.users = []
            self.library = []
            self.current_user = None

      def find_user(self, username):
            for u in self.users:
                  if u.username == username:
                        return u
            return None

      def register(self, username, password):
            if self.find_user(username):
                  print("username already exists.")
                  return None
            
            user = User(username, password)
            self.users.append(user)
            print(f"{username} registered successfully.")

            return user

      def login(self, username, password):
            user = self.find_user(username)
            if user and user.password == password:
                  self.current_user = user
                  print(f"welcome, {user.username}!")
            else:
                  print("you are not found...")

      def print_users(self):
            print("current users:")
            for u in self.users:
                  print(f"- {u.username}")

      def logout(self):
            if self.current_user:
                  print(f"goodbye {self.current_user.username}!")
                  self.current_user = None
            else:
                  print("user not logged in.")
