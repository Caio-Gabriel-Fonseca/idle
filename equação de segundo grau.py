import math
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
            Y= -B /(2*A)
            print ('O valor da raiz é {:.2f}'.format(Y))
        else:
            X=math.sqrt(DELTA)
            X1=(-B+X)/(2*A)
            X2=(-B-X)/(2*A)
            print ('O valor de X1 é {:.2f} e o valor de X2 é {:.2f}'.format(X1,X2))
            if (A > 0):
                print ('A concavidade é voltada para cima')
            else:
                print ('A concavidade é voltada para baixo')
                
                XV = -B / (2 * A)
                YV = -DELTA / (4 * A)
                print ('O vertice se encontra nos pontos: Xv em {:.2f} e Yv em {:.2f}'.format(XV,YV))
     
