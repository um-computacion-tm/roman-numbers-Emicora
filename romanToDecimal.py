
def roman_to_decimal(s: str) -> int:
    roman_decimal = {
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000,
    }
    result = 0
    ultimo_valor = 0
    for letter in s:
        valor_actual = roman_decimal[letter]
        result += valor_actual
        if ultimo_valor < valor_actual:
            result -= ultimo_valor * 2
        ultimo_valor = valor_actual
    return result


if __name__ == '__main__':
    print(roman_to_decimal("I"))
    
    
