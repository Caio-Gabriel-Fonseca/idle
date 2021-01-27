x=float(input('digite o primeiro numero:'))
y=float(input('digite o segundo numero:'))
""" {:.2f} eh pra mostrar so duas casas decimais """
if x == y:
    print('{:.2f} e {:.2f} são iguais.'.format(x,y))
else:
    if x<y:
        print('{:.2f} é menor que {:.2f} .'.format(x,y))
    else:
            print('{:.2f} é maior que {:.2f} .'.format(x,y))
