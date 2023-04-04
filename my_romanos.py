


def decimal_to_roman(decimal):
    numeros = [1000,900,500,400,100,90,50,40,10,9,5,4,1]
    letras = ["M","CM","D","CD","C","XC","L","XL","X","IX","V","IV","I"]

    result = ""

    i = 0

    while decimal > 0:
        for l in range(decimal//numeros[i]):
            result += letras[i]
            decimal -= numeros[i]
        i += 1

    return result

if __name__ == '__main__':
    print(decimal_to_roman(1))




