from models.product import TableProduct
from repository.abstract_repo import SQLRepository


class ProductRepository(SQLRepository):
    def __init__(self, model: TableProduct):
        self.model = model