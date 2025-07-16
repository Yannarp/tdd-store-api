from fastapi import FastAPI
from app.controllers import product_controller
from fastapi_pagination import add_pagination

app = FastAPI(title="TDD Store API")

app.include_router(product_controller.router)

@app.get("/")
async def root():
    return {"mensagem": "API funcionando! Vá para /docs"}

add_pagination(app)
