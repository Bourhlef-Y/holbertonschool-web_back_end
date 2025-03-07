#!/usr/bin/env python3
"""Module de tests unitaires pour utils.access_nested_map"""

import unittest
from parameterized import parameterized
from utils import access_nested_map


class TestAccessNestedMap(unittest.TestCase):
    """Classe de test pour la fonction access_nested_map"""

    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {"b": 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2),
    ])
    def test_access_nested_map(self, nested_map, path, expected):
        """Test que access_nested_map retourne la valeur attendue"""
        self.assertEqual(access_nested_map(nested_map, path), expected)
