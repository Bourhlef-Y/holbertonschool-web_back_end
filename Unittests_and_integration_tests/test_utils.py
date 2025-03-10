#!/usr/bin/env python3
"""Module de tests unitaires pour les fonctions utils"""

import unittest
from parameterized import parameterized
from utils import access_nested_map, get_json, memoize
from unittest.mock import patch
from typing import Dict, Tuple, Union


class TestAccessNestedMap(unittest.TestCase):
    """Classe de test pour la fonction access_nested_map"""

    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {"b": 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2),
    ])
    def test_access_nested_map(self, nested_map: Dict,
                             path: Tuple, expected: Union[Dict, int]) -> None:
        """Test que access_nested_map retourne la valeur attendue"""
        self.assertEqual(access_nested_map(nested_map, path), expected)

    @parameterized.expand([
        ({}, ("a",), "a"),
        ({"a": 1}, ("a", "b"), "b"),
    ])
    def test_access_nested_map_exception(
            self, nested_map: Dict, path: Tuple,
            expected_message: str) -> None:
        """Test que access_nested_map lève KeyError avec le bon message"""
        with self.assertRaises(KeyError) as context:
            access_nested_map(nested_map, path)
        self.assertEqual(str(context.exception), f"'{expected_message}'")


class TestGetJson(unittest.TestCase):
    """Classe de test pour la fonction get_json"""

    @parameterized.expand([
        ("http://example.com", {"payload": True}),
        ("http://holberton.io", {"payload": False}),
    ])
    def test_get_json(self, test_url: str, test_payload: Dict) -> None:
        """Test que get_json retourne le payload attendu"""
        with patch('requests.get') as mock_get:
            mock_get.return_value.json.return_value = test_payload
            result = get_json(test_url)
            mock_get.assert_called_once_with(test_url)
            self.assertEqual(result, test_payload)


class TestMemoize(unittest.TestCase):
    """Classe de test pour le décorateur memoize"""

    def test_memoize(self) -> None:
        """Test que la méthode décorée n'est appelée qu'une seule fois"""
        class TestClass:
            """Classe de test pour la mémoïsation"""
            def a_method(self) -> int:
                """Méthode retournant une valeur fixe"""
                return 42

            @memoize
            def a_property(self) -> int:
                """Propriété mémoïsée appelant a_method"""
                return self.a_method()

        with patch.object(TestClass, 'a_method') as mock_method:
            test_class = TestClass()
            mock_method.return_value = 42

            first_call = test_class.a_property
            second_call = test_class.a_property

            self.assertEqual(first_call, 42)
            self.assertEqual(second_call, 42)
            mock_method.assert_called_once()
