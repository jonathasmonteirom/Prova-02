def q1(): #cidades
    def cidades(idades):
    
        cidades = []
        for cidade, idade in idades.items():
            if idade > 100:
                cidades.append(cidade)
        return cidades

    idades = {
        "João Pessoa": 432,
        "Campina Grande": 325,
        "Santa Rita": 68,
        "Patos": 289,
        "Bayeux": 54,
        "Sousa": 178,
        "Cajazeiras": 201,
        "Cabedelo": 45,
        "Guarabira": 122,
        "Areia": 177,
        }

    resultado = cidades(idades)
    print(resultado)
    return [] 

def q2(): #lista1, lista2
    def listas(lista1, lista2):
        unidas = lista1 + lista2

        positivos = [x for x in unidas if x > 0]

        soma = sum(positivos)

        ordenada = sorted(positivos)

        return (soma, ordenada)

    lista1 = [3, -5, 12, 0, -8, 7]
    lista2 = [-2, 10, -1, 6, -4, 9]

    resultado = listas(lista1, lista2)
    print(resultado)
    return []

def q3(): #valores
    def lerValores():
        lista = []
        while True:
            valor = int(input("Digite um número (0 para parar): "))
            if valor == 0:
                break
            lista.append(valor)
        return lista

    def processaLista(lista):
        pares = []
        impares = []
        for num in lista:
            if num % 2 == 0:
                pares.append(num)
            else:
                impares.append(num)
        return pares, impares

    valores = lerValores()
    listaPares, listaImpares = processaLista(valores)

    print("Lista de Pares:", listaPares)
    print("Lista de Ímpares:", listaImpares)
    return [],[]

def q4(): #valores
    def organizarAlturas(lista):
        ordenado = sorted(lista)
        return [ordenado[1], ordenado[2], ordenado[0]]

    def formatarAlturas(lista):
        return [f"{altura:.2f}" for altura in lista]

    valores = [30, 20, 10]

    alturasOrganizadas = organizarAlturas(valores)
    alturasFormatadas = formatarAlturas(alturasOrganizadas)

    print('[' + ', '.join(f'"{a}"' for a in alturasFormatadas) + ']')
    return []

def main():
    # Teste as questões que você desenvolveu manualmente:
    idades = {
        "João Pessoa": 432,
        "Campina Grande": 325,
        "Santa Rita": 68,
        "Patos": 289,
        "Bayeux": 54,
        "Sousa": 178,
        "Cajazeiras": 201,
        "Cabedelo": 45,
        "Guarabira": 122,
        "Areia": 177,
    }
    resultado = q1(idades)
    print("q1:", resultado)


    lista1 = [3, -5, 12, 0, -8, 7]
    lista2 = [-2, 10, -1, 6, -4, 9]
    resultado = q2(lista1, lista2)
    print("q2:", resultado)



if __name__ == "__main__":
    q1()


