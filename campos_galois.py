import numpy as np
import galois as gg

GF256 = gg.GF(2**8)
print(GF256)

x = GF256(["y**6 + 1", 0, 2, "1", "y**5 + y**4 + y"])

print(f'Conjunto de elementos: y^6 + 1\nOperador aditivo: 0\nOperador multiplicativo: 2\nIdentidad aditiva: 1\nIdentidad multiplicativa: y^5 + y^4 + y')
print(x)
GF = gg.GF(36893488147419103183)
print(GF.properties)

