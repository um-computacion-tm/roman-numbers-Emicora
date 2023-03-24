import unittest

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
    
    
if __name__=="__main__":
    unittest.main()