models.py

from pydantic import BaseModel

class ProductosRequest(BaseModel):
    codigos: list[str]