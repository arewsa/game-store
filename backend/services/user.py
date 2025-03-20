from models.user import AddUser
from schemas.user import User, UserInSystem
from repository.abstract_repo import AbstractRepository


class UserService:
    def __init__(self, users_repository: AbstractRepository):
        self.users_repository: AbstractRepository = users_repository

    def add_user(self, user: AddUser) -> User:
        user = AddUser(user)
        user_data = user.get_data()
        return self.users_repository.add(user_data)
    
    def get_user(self, email: str) -> UserInSystem:
        data = self.users_repository.get(email, "user_id, mail, password")
        user: UserInSystem = UserInSystem(user_id=data[0], login=data[1], password=data[2])
        return user
    
    def get_all_users(self) -> list[UserInSystem]:
        users: list[UserInSystem] = []
        for user in self.users_repository.get_all(string_of_param="user_id, mail, password"):
            users.append(UserInSystem(user_id=user[0], login=user[1], password=user[2]))
        return users