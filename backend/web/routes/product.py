from typing import Annotated
from fastapi import APIRouter, Depends, Query, Request
from schemas.product import Game, Product
from services.product import ProductService
from web.routes.dependencies import authorize, game_service

router = APIRouter(prefix="/product", tags=["Products"])

@router.get("/games", status_code=200)
async def get_games(request: Request, product_service: ProductService = Depends(game_service)):
    return product_service.get_all_products(Game)

@router.post("/game", status_code=200)
async def add_game(game: Product, product_service: ProductService = Depends(game_service)):
    return product_service.add_product(game)

@router.get("games/shopping_cart", status_code=200)
async def list_of_game_in_cart(list_of_id: Annotated[list[int], Query()], product_service: ProductService = Depends(game_service)):
    list_of_games = product_service.get_product_in_shopping_cart(list_of_id=list_of_id, product_class=Game)
    return list_of_games