import unittest
from TestUtils import TestAST
from AST import *


class ASTGenSuite(unittest.TestCase):
    def test(self):
        input = """x: array [0] of integer = {};"""
        expect = ""
        self.assertTrue(TestAST.test(input, expect, 300))
