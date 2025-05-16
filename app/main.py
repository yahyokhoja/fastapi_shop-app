from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from app.routes import store  # у
from app.routes import auth_router, store_router, user_router, shop_router, product_router, order_router

app = FastAPI()

app.mount("/static", StaticFiles(directory="app/static"), name="static")
templates = Jinja2Templates(directory="app/templates")
app.include_router(store.router)
app.include_router(auth_router, tags=["auth"])
app.include_router(store_router, tags=["store"])
app.include_router(user_router, prefix="/users", tags=["users"])
app.include_router(shop_router, prefix="/shops", tags=["shops"])
app.include_router(product_router, prefix="/products", tags=["products"])
app.include_router(order_router, prefix="/orders", tags=["orders"])

@app.get("/", response_class=HTMLResponse)
def read_root(request: Request):
    return templates.TemplateResponse("index.html", {"request": request, "msg": "Добро пожаловать!"})
