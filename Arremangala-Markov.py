tokens = ['otro', 'ay', 'arremángala', 'arrempújala', 'sí', 'no', 'fin']
letra = []

archivo = open('Arremangala-letra.txt')

letra = archivo.read().replace(' ', '').split(',')

#Cálculo de probabilidades
#Otra -> Otra, Ay, Arremángala, Arrempújala, Fin
#Ay -> Arremángala
#Arremángala -> Arrempújala, otro
#Arrempújala -> Arremángala, Sí, No, Otra
#Sí -> Arremángala, otro
#No -> Arremángala
probabilidadesPares = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
totalPares = 0
probabilidadesTokens = [0,0,0,0,0,0,0]
totalTokens = 0
combinacion = 'otro,otro'
combinaciones = ['otro,otro', 'otro,ay', 'otro,arremángala', 'otro,arrempújala' ,'otro,fin', 'ay,arremángala', 'arremángala,arrempújala', 'arremángala,otro' ,'arrempújala,arremángala', 'arrempújala,sí', 'arrempújala,no', 'arrempújala,otro', 'sí,arremángala', 'sí,otro', 'no,arremángala']

TAM_LETRA = len(letra)

for i in range(TAM_LETRA):
    if (letra[i].lower() not in tokens):
        letra[i] = 'otro'
    else:
        letra[i] = letra[i].lower()
letra[-1] = 'fin'#@daredliuth: Creo que como ya se añadió fin a los tokens esto se puede quitar.

for i in range(TAM_LETRA):
    if(i < TAM_LETRA-1):
        #print(f"{letra[i]} -> {letra[i+1]}")
        #print(f"\n[{i}]Combinación: \n\t{combinacion}\n\nÍndice: {combinaciones.index(combinacion)}")
        combinacion = letra[i] + ',' + letra[i+1]
        probabilidadesPares[combinaciones.index(combinacion)] += 1
    probabilidadesTokens[tokens.index(letra[i])] += 1

#Obtención de las probabilidades para cada token.
print('*****PROBABILIDADES TOKENS*****')
for i in range(len(probabilidadesTokens)):
    totalTokens += probabilidadesTokens[i]
for i in range(len(probabilidadesTokens)):
    print(f"{tokens[i]}: {probabilidadesTokens[i]/totalTokens}")
    probabilidadesTokens[i] = probabilidadesTokens[i]/totalTokens

#Obtención de las porbabilidades para cada par.
print('\n*****PROBABILIDADES PARES*****')
for i in range(len(probabilidadesPares)):
    totalPares += probabilidadesPares[i]
for i in range(len(probabilidadesPares)):
    print(f"{combinaciones[i]}: {probabilidadesPares[i]/totalPares}")
    probabilidadesPares[i] = probabilidadesPares[i]/totalPares

for token in tokens:
    print(f'\nToken: {token}')
    for combinacion in combinaciones:
        if token in combinacion.split(',')[0]:
            print(f'Combinación: {combinacion}\tProbabilidad:: {probabilidadesPares[combinaciones.index(combinacion)] / probabilidadesTokens[tokens.index(token)]}')
