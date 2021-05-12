# Faça um programa que calcule o salário de um colaborador na empresa XYZ. O salário é pago conforme a quantidade de horas trabalhadas. Quando um funcionário trabalha mais de 40 horas ele recebe um adicional de 1.5 nas horas extras trabalhadas.
#

def adjSal(perHour, hours):
    if hours > 40:
        salary = (perHour * 40) + ((hours - 40) * perHour * 1.5)
    else:
        salary = (perHour * hours)
    return salary


v = adjSal(20, 50)
print(v)
