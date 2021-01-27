sal = float(input('Qual é o salário do funcionario? R$'))
novo = sal + (sal * 15 / 100)
print('Um funcionario que receebia R${:.2f}, com um aumento de 15% fica R${:.2f}'.format(sal, novo))
