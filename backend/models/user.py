from schemas.user import CreateUser
import bcrypt


class TableInfo():
    tablename: str
    string_of_columns: str
    obj_id_column: str

class AddUser():
    def __init__(self, user: CreateUser):
        self.name = user.name
        self.surname = user.surname
        self.email = user.email
        self.hashed_password = bcrypt.hashpw(password=user.password.encode(), salt=bcrypt.gensalt()).decode()


    def get_data(self) -> tuple:
        return (self.name, self.surname, self.email, self.hashed_password)

class TableUser(TableInfo):
    tablename = "users"
    string_of_columns = "name, surname, mail, password"
    obj_id_column = "mail"