from typing import Generator
from unittest import TestCase
from unittest.mock import MagicMock

from regex_search.regex_search import juntar_nomes_de_arquivos


class Testes(TestCase):
    def test_retornando_um_generator_caso_a_pasta_exista(self):
        resultado = juntar_nomes_de_arquivos('.')
        self.assertIsInstance(resultado, Generator)

    def test_retornando_um_generator_caso_a_pasta_nao_exista(self):
        resultado = juntar_nomes_de_arquivos('esta_pasta_não_existe')
        self.assertIsInstance(resultado, Generator)

    def test_retornando_os_arquivos_dentro_da_pasta_regex_search(self):
        resultado = tuple(juntar_nomes_de_arquivos('regex_search'))
        esperado = (
            'regex_search/__init__.py',
            'regex_search/regex_search.py',
            'regex_search/__pycache__/__init__.cpython-37.pyc',
            'regex_search/__pycache__/regex_search.cpython-37.pyc'
        )
        self.assertEqual(resultado, esperado)
