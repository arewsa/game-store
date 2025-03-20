from fastapi import FastAPI
from web.routes.user import router as user_router
from web.routes.product import router as product_router

app = FastAPI()

app.include_router(user_router)
app.include_router(product_router)