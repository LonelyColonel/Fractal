from fastapi import FastAPI
from app.api.router import router

app = FastAPI(title="Compression API Gateway")
app.include_router(router)
