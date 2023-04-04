import unittest
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

class TestRomanToInt(unittest.TestCase):
    def test_simple(self):
        self.assertEqual(roman_to_decimal("I"), 1)
        self.assertEqual(roman_to_decimal("V"), 5)
        self.assertEqual(roman_to_decimal("X"), 10)
        self.assertEqual(roman_to_decimal("L"), 50)
        self.assertEqual(roman_to_decimal("C"), 100)
        self.assertEqual(roman_to_decimal("D"), 500)
        self.assertEqual(roman_to_decimal("M"), 1000)
    def test_suma(self):
        self.assertEqual(roman_to_decimal("II"), 2)
        self.assertEqual(roman_to_decimal("VI"), 6)
        self.assertEqual(roman_to_decimal("XIII"), 13)
        self.assertEqual(roman_to_decimal("LX"), 60)
        self.assertEqual(roman_to_decimal("MMXXI"), 2021)
    def test_resta(self):
        self.assertEqual(roman_to_decimal("IV"), 4)
        self.assertEqual(roman_to_decimal("IX"), 9)
        self.assertEqual(roman_to_decimal("XL"), 40)
        self.assertEqual(roman_to_decimal("XC"), 90)
        self.assertEqual(roman_to_decimal("CD"), 400)
        self.assertEqual(roman_to_decimal("CM"), 900)
    
if __name__ == '__main__':
    unittest.main()

