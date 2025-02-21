#!/usr/bin/env python3
"""
Authentication module for the API.
"""
from flask import request
from typing import List, TypeVar


class Auth:
    """
    Authentication class to manage API authentication.
    """

    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """
        Determines whether a path requires authentication.
        Args:
            path (str): URL path to check
            excluded_paths (List[str]): List of paths that don't require
                authentication
        Returns:
            bool: True if authentication is required, False otherwise
        """
        return False

    def authorization_header(self, request=None) -> str:
        """
        Gets the authorization header from the request.
        Args:
            request: Flask request object
        Returns:
            str: Value of the Authorization header or None
        """
        return None

    def current_user(self) -> TypeVar('User'):
        """
        Gets the current user from the request.
        Returns:
            TypeVar('User'): Current user or None
        """
        return None
