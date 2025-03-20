from models.product import AddProduct
from schemas.product import Product
from repository.abstract_repo import AbstractRepository


class ProductService:
    def __init__(self, product_repository: AbstractRepository):
        self.product_repository = product_repository

    def get_all_products(self, product_class: Product) -> list[Product]:
        products: list[Product] = []
        for product in self.product_repository.get_all():
            products.append(product_class(product_id=product[0], name=product[1], price=product[2], img=product[3]))
        return products

    def add_product(self, product: Product):
        return self.product_repository.add(
            AddProduct(name=product.name, price=product.price, img=product.img).get_data()
        )

    def get_product_in_shopping_cart(self, list_of_id: list[int], product_class: Product):
        products: list[Product] = []
        for product in self.product_repository.get_by_id(obj_ids=list_of_id):
            products.append(product_class(product_id=product[0], name=product[1], price=product[2], img=product[3]))
        return products