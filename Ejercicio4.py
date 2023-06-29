"""En 2022 el paıs A tendra una poblacion de 25 millones de habitantes
y el paıs B de 18.9 millones. Las tasas de crecimiento anual de la
poblacion seran de 2% y 3% respectivamente. Desarrollar un
programa que imprima el ano en que la poblacion del paıs B superara
a la de A.
"""

Anio=2022
poblacionA=25
poblacionB=18.9
tasaA=0.02
tasaB=0.03

while poblacionA >= poblacionB:
    poblacionA += poblacionA * tasaA
    poblacionB += poblacionB * tasaB
    Anio += 1

print("el ano en que la poblacion del pais B superara la de A:", Anio)
