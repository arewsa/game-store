from models.user import TableUser
from repository.abstract_repo import SQLRepository


class UserRepository(SQLRepository):
    model = TableUser