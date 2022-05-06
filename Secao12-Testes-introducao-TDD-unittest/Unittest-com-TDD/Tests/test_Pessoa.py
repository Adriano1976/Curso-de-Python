"""
class Pessoa
    __init__
        nome str
        sobrenome str
        dados_obtidos bool (inicia false)

    API:
        obter_todos_os_dados -> method
            OK
            404

            (dados_obtidos se torna True se dados obtidos com sucesso.)
"""
import unittest
from unittest.mock import patch

from Pessoa import Pessoa


class TestPessoa(unittest.TestCase):
    def setUp(self):
        self.p1 = Pessoa('Adriano', 'Santos')
        self.p2 = Pessoa('Neide', 'Ferreira')

    def test_Pessoa_attr_nome_tem_o_valor_correto(self):
        self.assertEqual(self.p1.nome, 'Adriano')
        self.assertEqual(self.p2.nome, 'Neide')

    def test_Pessoa_attr_nome_e_str(self):
        self.assertIsInstance(self.p1.nome, str)
        self.assertIsInstance(self.p2.nome, str)

    def test_Pessoa_attr_sobrenome_tem_o_valor_correto(self):
        self.assertEqual(self.p1.sobrenome, 'Santos')
        self.assertEqual(self.p2.sobrenome, 'Ferreira')

    def test_Pessoa_attr_sobrenome_e_str(self):
        self.assertIsInstance(self.p1.sobrenome, str)
        self.assertIsInstance(self.p2.sobrenome, str)

    def test_Pessoa_attr_dados_obtidos_inicia_false(self):
        self.assertFalse(self.p1.dados_obtidos)
        self.assertFalse(self.p2.dados_obtidos)

    def test_obter_todos_os_dados_sucesso_OK(self):
        with patch('requests.get') as fake_request:
            fake_request.return_value.ok = True

            self.assertEqual(self.p1.obter_todos_os_dados(), 'CONECTADO')
            self.assertTrue(self.p1.dados_obtidos)
            self.assertEqual(self.p2.obter_todos_os_dados(), 'CONECTADO')
            self.assertTrue(self.p2.dados_obtidos)

    def test_obter_todos_os_dados_falha_404(self):
        with patch('requests.get') as fake_request:
            fake_request.return_value.ok = False

            self.assertEqual(self.p1.obter_todos_os_dados(), 'Erro 404')
            self.assertFalse(self.p1.dados_obtidos)
            self.assertEqual(self.p2.obter_todos_os_dados(), 'Erro 404')
            self.assertFalse(self.p2.dados_obtidos)

    def test_obter_todos_os_dados_sucesso_e_falha_sequencial(self):
        with patch('requests.get') as fake_request:
            fake_request.return_value.ok = True

            self.assertEqual(self.p1.obter_todos_os_dados(), 'CONECTADO')
            self.assertTrue(self.p1.dados_obtidos)
            self.assertEqual(self.p2.obter_todos_os_dados(), 'CONECTADO')
            self.assertTrue(self.p2.dados_obtidos)

            fake_request.return_value.ok = False

            self.assertEqual(self.p1.obter_todos_os_dados(), 'Erro 404')
            self.assertFalse(self.p1.dados_obtidos)
            self.assertEqual(self.p2.obter_todos_os_dados(), 'Erro 404')
            self.assertFalse(self.p2.dados_obtidos)


if __name__ == '__main__':
    unittest.main(verbosity=2)
