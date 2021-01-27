coisa = input ('Digite algo')

print ('O tipo primitivo do que você digitou é', type(coisa))
print ('O  que você digitou tem spaços?', coisa.isspace())
print ('O  que você digitou tem numeros?', coisa.isnumeric())
print ('O  que você digitou tem letras?', coisa.isalpha())
print ('O  que você digitou tem letras e numeros?', coisa.isalnum())
