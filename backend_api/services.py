services.py

def generar_precio(codigo: str) -> float:
    base = sum(ord(c) for c in codigo)
    return round(50000 + (base % 5000), 2)

def generar_stock(codigo: str) -> int:
    return (sum(ord(c) for c in codigo) % 50) + 1