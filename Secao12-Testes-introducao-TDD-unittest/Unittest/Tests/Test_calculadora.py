import unittest

from Calculator import sum


class TestCalculator(unittest.TestCase):
    def test_sum_5_e_5_deve_retornar_10(self):
        self.assertEqual(sum(5, 5), 10)

    def test_sum_5_negativo_e_5_deve_retornar_0(self):
        self.assertEqual(sum(-5, 5), 0)

    def test_sum_varias_entradas(self):
        x_y_saidas = (
            (10, 10, 20),
            (5, 5, 10),
            (1.5, 1.5, 3.0),
            (-5, 4, -1),
            (100, 100, 200),
        )

        for x_y_saida in x_y_saidas:
            with self.subTest(x_y_saida=x_y_saida):
                x, y, saida = x_y_saida
                self.assertEqual(sum(x, y), saida)

    def test_sum_x_nao_e_int_ou_float_deve_retornar_assertionerror(self):
        with self.assertRaises(AssertionError):
            sum('11', 0)

    def test_sum_y_nao_e_int_ou_float_deve_retornar_assertionerror(self):
        with self.assertRaises(AssertionError):
            sum(11, '0')


if __name__ == "__main__":
    unittest.main(verbosity=2)
