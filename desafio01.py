lista=[]
erros=[]
while True:
    try:
        qntos=int(input("Quantos Tracajás?(1-50 tracajás)\n"))
        if qntos >=1 and qntos <=50:
            for i in range (qntos):
                lista.append(int(input("Velocidade(1-25 km/h): ")))
            break                
        else:
            print("Valor inválido de tracajás.")
            exit()
    except ValueError: print("ERROR. Reiniciando...")
nvl=0
for i in range (len(lista)):
    if lista[i]>25 or lista[i]<1: 
        erros.append(i+1)
    elif lista[i]<10 and nvl<1:nvl=1
    elif lista[i]>=10 and lista[i]<15 and nvl<2:nvl=2
    elif lista[i]>=15 and nvl<3:nvl=3
if erros==[]: print(nvl)
else:
    for i in erros: print(f'Valor inválido na linha {i}')
