media = float(input('Informe o valor de sua nota final:'))
if(media >= 8):
    print('Você foi aprovado com louvor.')
elif(5 <=media < 8):
    print('você esta aprovado')
elif(3.5 <=media < 5):
    print('você esta de recuperação')
else:
    print('Você esta reprovado')
