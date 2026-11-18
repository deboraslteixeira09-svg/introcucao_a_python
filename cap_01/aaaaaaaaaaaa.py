vt = float (input("Valor Total: "))
dc = float (input("Desconto: "))
dc = dc / 100
vtcdc = vt - (dc * vt)
print(f"Valor com Desconto {vtcdc}")
