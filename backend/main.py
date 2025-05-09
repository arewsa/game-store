from fastapi import FastAPI
from web.routes.user import router as user_router
from web.routes.product import router as product_router
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

origins = [
    "http://localhost",
    "http://localhost:5173",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],    
)

app.include_router(user_router)
app.include_router(product_router)