A = float(input('Digite o valor de A:'))
B = float(input('Digite o valor de B:'))
C = float(input('Digite o valor de C:'))
DELTA = (B**2)-(4*A*C)

if (A==0):
    print ('Não é uma equação de segundo grau')
else:
    if (DELTA < 0):
        print ('Não possui raizes reais')
    else:
        if (DELTA == 0):
            X = -B / (2 * A)
            print ('O valor é {}'.format (x))
        else:
            X1=(-B+sqrt(DELTA))/(2*A)
            X2=(-B-sqrt(DELTA))/(2*A)
