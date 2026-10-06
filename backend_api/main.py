main.py

from fastapi import FastAPI

from app.services import generar_precio, generar_stock
from app.models import ProductosRequest

app = FastAPI()

@app.post("/productos")
def obtener_productos_batch(request: ProductosRequest):

    resultado = []

    for codigo in request.codigos:

        resultado.append({
            "codigo": codigo,
            "precio": generar_precio(codigo),
            "stock": generar_stock(codigo)
        })

    return resultado