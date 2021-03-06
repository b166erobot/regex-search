from typing import Generator
from unittest import TestCase
from unittest.mock import MagicMock, patch

from regex_search.regex_search import procurar_no_arquivo


class Testes(TestCase):
    def setUp(self):
        self.args = [r'teste_retornando_esse_metodo', # <- not test, why?
                     'tests/teste_regex_search_funcao_procurar_no_arquivo.py']
        self.mocks = [MagicMock(), MagicMock()]

    def test_retornando_esse_metodo(self):
        regex = 'test_retornando_esse_metodo'
        resultado = next(procurar_no_arquivo(regex, *self.args[1:]))
        esperado = ('    def \x1b[38;5;208mtest_retornando_esse_metodo\x1b['
                    '0m(self):\n')
        self.assertIn(esperado, resultado)

    @patch('regex_search.regex_search.search', return_value = True)
    def test_retornando_um_generator_caso_search_retorne_algo(self, _):
        resultado = procurar_no_arquivo(*self.args)
        self.assertIsInstance(resultado, Generator)

    @patch('regex_search.regex_search.search', return_value = False)
    def test_retornando_um_generator_caso_search_nao_retorne_algo(self, _):
        resultado = procurar_no_arquivo(*self.args)
        self.assertIsInstance(resultado, Generator)

    @patch('regex_search.regex_search.open')
    def test_raise_um_UnicodeDecodeError_e_retornando_generator(self, open):
        open.side_effect = UnicodeDecodeError('', b'', 1, 2, '')
        resultado = procurar_no_arquivo(*self.args)
        self.assertIsInstance(resultado, Generator)
