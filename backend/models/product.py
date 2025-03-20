from models.user import TableInfo

class TableProduct(TableInfo):
    tablename: str
    string_of_columns: str
    obj_id_column: str
    obj_id: str

class TableGame(TableProduct):
    tablename = "games_cards"
    string_of_columns = "game_name, game_price, game_img"
    obj_id_column = "game_name"
    obj_id = "product_id"


class AddProduct():
    def __init__(self, name: str, price: int, img: str):
        self.name = name
        self.price = price
        self.img = img

    def get_data(self):
        return (self.name, self.price, self.img)