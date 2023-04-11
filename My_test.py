import unittest

from my_romanos import decimal_to_roman
from romanToDecimal import roman_to_decimal

class TestDecimalToRomano(unittest.TestCase):
    def test_1(self):

        resultado = decimal_to_roman(1)

        self.assertEqual(resultado,"I")

    def test_10(self):

        resultado = decimal_to_roman(10)

        self.assertEqual(resultado,"X")

    def test_5(self):

        resultado = decimal_to_roman(5)

        self.assertEqual(resultado,"V")
    
    def test_2(self):

        resultado = decimal_to_roman(2)

        self.assertEqual(resultado,"II")

    def test_3(self):

        resultado = decimal_to_roman(3)

        self.assertEqual(resultado,"III")
    
    def test_4(self):

        resultado = decimal_to_roman(4)

        self.assertEqual(resultado,"IV")

    def test_6(self):

        resultado = decimal_to_roman(6)

        self.assertEqual(resultado,"VI")

    def test_7(self):

        resultado = decimal_to_roman(7)

        self.assertEqual(resultado,"VII")

    def test_8(self):

        resultado = decimal_to_roman(8)

        self.assertEqual(resultado,"VIII")

    def test_44(self):

        resultado = decimal_to_roman(44)

        self.assertEqual(resultado,"XLIV")

    def test_59(self):

        resultado = decimal_to_roman(59)

        self.assertEqual(resultado,"LIX")

    def test_94(self):

        resultado = decimal_to_roman(94)

        self.assertEqual(resultado,"XCIV")

    def test_584(self):

        resultado = decimal_to_roman(584)

        self.assertEqual(resultado,"DLXXXIV")

    def test_767(self):

        resultado = decimal_to_roman(767)

        self.assertEqual(resultado,"DCCLXVII")

    def test_999(self):

        resultado = decimal_to_roman(999)

        self.assertEqual(resultado,"CMXCIX")

    def test_1000(self):

        resultado = decimal_to_roman(1000)

        self.assertEqual(resultado,"M")
        
    def test_simple1(self):
        self.assertEqual(roman_to_decimal("I"), 1)
    def test_simple2(self):
        self.assertEqual(roman_to_decimal("V"), 5)
    def test_simple3(self):
        self.assertEqual(roman_to_decimal("X"), 10)
    def test_simple4(self):
        self.assertEqual(roman_to_decimal("L"), 50)
    def test_simple5(self):
        self.assertEqual(roman_to_decimal("C"), 100)
    def test_simple6(self):
        self.assertEqual(roman_to_decimal("D"), 500)
    def test_simple7(self):
        self.assertEqual(roman_to_decimal("M"), 1000)

    def test_suma1(self):
        self.assertEqual(roman_to_decimal("II"), 2)
    def test_suma2(self):
        self.assertEqual(roman_to_decimal("VI"), 6)
    def test_suma3(self):
        self.assertEqual(roman_to_decimal("XIII"), 13)
    def test_suma4(self):
        self.assertEqual(roman_to_decimal("LX"), 60)
    def test_suma5(self):
        self.assertEqual(roman_to_decimal("MMXXI"), 2021)

    def test_resta1(self):
        self.assertEqual(roman_to_decimal("IV"), 4)
    def test_resta2(self):
        self.assertEqual(roman_to_decimal("IX"), 9)
    def test_resta3(self):
        self.assertEqual(roman_to_decimal("XL"), 40)
    def test_resta4(self):
        self.assertEqual(roman_to_decimal("XC"), 90)
    def test_resta5(self):
        self.assertEqual(roman_to_decimal("CD"), 400)
    def test_resta6(self):
        self.assertEqual(roman_to_decimal("CM"), 900)
    
if __name__=="__main__":
    unittest.main()