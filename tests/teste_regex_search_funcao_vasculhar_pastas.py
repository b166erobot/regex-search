from typing import Generator
from unittest import TestCase
from unittest.mock import MagicMock, patch

from regex_search.regex_search import vasculhar_pastas


class Testes(TestCase):
    def setUp(self):
        self.args = ('def|class', 'tests', False)

    def test_retornando_um_gerador(self):
        resultado = vasculhar_pastas(*self.args)
        self.assertIsInstance(resultado, Generator)

    def test_retornando_essa_classe(self):
        resultado = vasculhar_pastas(*self.args)
        esperado = '\x1b[38;5;208mclass\x1b[0m Testes(TestCase):\n'
        next(resultado)
        self.assertIn(esperado, next(resultado))

    @patch('regex_search.regex_search.procurar_no_arquivo', return_value=False)
    def test_retornando_um_generator_caso_resultado_seja_false(self, _):
        resultado = vasculhar_pastas(*self.args)
        self.assertIsInstance(resultado, Generator)

    @patch('regex_search.regex_search.procurar_no_arquivo')
    def test_raise_StopIteration_retornando_generator(self, proc):
        proc.return_value = MagicMock(side_effect = StopIteration())
        resultado = vasculhar_pastas(*self.args)
        self.assertIsInstance(resultado, Generator)
