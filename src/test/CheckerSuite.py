import unittest
from TestUtils import TestChecker
from AST import *


class CheckerSuite(unittest.TestCase):
    def test0(self):
        input = """a: integer;
        c: float;
        a: float;"""
        expect = "No entry point"
        self.assertTrue(TestChecker.test(input, expect, 400))

    def test1(self):
        input = """a: integer;
        c: float;"""
        expect = "No entry point"
        self.assertTrue(TestChecker.test(input, expect, 401))

    def test2(self):
        input = """a: integer = 4;
        c: float;
        main: function void () {}
        a: string;"""
        expect = "Redeclared Variable: a"
        self.assertTrue(TestChecker.test(input, expect, 402))

    def test3(self):
        input = """a: integer = 4;
        c: auto;
        main: function void () {}"""
        expect = "Invalid Variable: c"
        self.assertTrue(TestChecker.test(input, expect, 403))

    def test4(self):
        input = """a: array [3] of integer = {1,2};
        main: function void () {}"""
        expect = "Type mismatch in Variable Declaration: VarDecl(a, ArrayType([3], IntegerType), ArrayLit([IntegerLit(1), IntegerLit(2)]))"
        self.assertTrue(TestChecker.test(input, expect, 404))

    def test5(self):
        input = """a: array [2] of float = {1.0 , "string"};
        main: function void () {}"""
        expect = "Illegal array literal: ArrayLit([FloatLit(1.0), StringLit(string)])"
        self.assertTrue(TestChecker.test(input, expect, 405))

    def test6(self):
        input = """a: array [2] of float = {"string", "string"};
        main: function void () {}"""
        expect = "Type mismatch in Variable Declaration: VarDecl(a, ArrayType([2], FloatType), ArrayLit([StringLit(string), StringLit(string)]))"
        self.assertTrue(TestChecker.test(input, expect, 406))

    def test7(self):
        input = """a: integer = 2 + 3;
        b: float = a + 3.2;
        c: integer = b;
        main: function void () {}"""
        expect = "Type mismatch in Variable Declaration: VarDecl(c, IntegerType, Id(b))"
        self.assertTrue(TestChecker.test(input, expect, 407))

    def test8(self):
        input = """a: integer = 5 + 4;
        b: float = 3.0;
        q: boolean = true || false;
        c: integer = a % b;
        main: function void () {}"""
        expect = "Type mismatch in expression: BinExpr(%, Id(a), Id(b))"
        self.assertTrue(TestChecker.test(input, expect, 408))

    def test9(self):
        input = """a: integer = 5 + 4;
        b: float = 3.0;
        c: string = "string" :: "string";
        g: boolean = 1 < 3.0;
        q: boolean = true && 1;
        main: function void () {}"""
        expect = "Type mismatch in expression: BinExpr(&&, BooleanLit(True), IntegerLit(1))"
        self.assertTrue(TestChecker.test(input, expect, 409))

    def test10(self):
        input = """a: array [2, 3] of integer = {{1, 2, 3}, {1, 3, 4}};
        c: array [3] of integer = a[1];
        b: array [1, 3] of integer = {{1, 2, 3}, {1, 3, 4}};
        main: function void () {}"""
        expect = "Type mismatch in Variable Declaration: VarDecl(b, ArrayType([1, 3], IntegerType), ArrayLit([ArrayLit([IntegerLit(1), IntegerLit(2), IntegerLit(3)]), ArrayLit([IntegerLit(1), IntegerLit(3), IntegerLit(4)])]))"
        self.assertTrue(TestChecker.test(input, expect, 410))

    def test11(self):
        input = """a: array [2,2] of integer = {{1, 2}, {"string", "string"}};
        main: function void () {}"""
        expect = "Illegal array literal: ArrayLit([ArrayLit([IntegerLit(1), IntegerLit(2)]), ArrayLit([StringLit(string), StringLit(string)])])"
        self.assertTrue(TestChecker.test(input, expect, 411))

    def test12(self):
        input = """a: array [2,2] of integer = {{1, 2, 3}, {1, 2}};
        main: function void () {}"""
        expect = "Illegal array literal: ArrayLit([ArrayLit([IntegerLit(1), IntegerLit(2), IntegerLit(3)]), ArrayLit([IntegerLit(1), IntegerLit(2)])])"
        self.assertTrue(TestChecker.test(input, expect, 412))

    def test13(self):
        input = """a: array [2,2] of integer = {{2, 3}, {1, 2}};
        b: integer = c[0];
        main: function void () {}"""
        expect = "Undeclared Identifier: c"
        self.assertTrue(TestChecker.test(input, expect, 413))

    def test14(self):
        input = """a: array [2,2] of integer = {{2, 3}, {1, 2}};
        b: integer = 20;
        c: integer = b[1];
        main: function void () {}"""
        expect = "Type mismatch in expression: ArrayCell(b, [IntegerLit(1)])"
        self.assertTrue(TestChecker.test(input, expect, 414))

    def test15(self):
        input = """a: array [2] of integer = {1, 2};
        b: integer = a[1, 2];
        main: function void () {}"""
        expect = "Type mismatch in expression: ArrayCell(a, [IntegerLit(1), IntegerLit(2)])"
        self.assertTrue(TestChecker.test(input, expect, 415))

    def test16(self):
        input = """a: array [2] of integer = {1, 2};
        b: integer = a["string"];
        main: function void () {}"""
        expect = "Type mismatch in expression: ArrayCell(a, [StringLit(string)])"
        self.assertTrue(TestChecker.test(input, expect, 416))

    def test17(self):
        input = """a: array [2] of integer = {1, 2};
        b: float = a[1];
        main: function void () {}"""
        expect = "Type mismatch in Variable Declaration: VarDecl(b, FloatType, ArrayCell(a, [IntegerLit(1)]))"
        self.assertTrue(TestChecker.test(input, expect, 417))

    def test18(self):
        input = """a: array [2, 2, 1] of integer = {{{1},{3}}, {{1},{4}}};
        c: array [2, 1] of integer = a[0];
        b: float = a[1];
        main: function void () {}"""
        expect = "Type mismatch in Variable Declaration: VarDecl(b, FloatType, ArrayCell(a, [IntegerLit(1)]))"
        self.assertTrue(TestChecker.test(input, expect, 418))

    def test19(self):
        input = """a: float = 3.0;
        test: function integer (c: integer, d: integer) {}
        b: integer = nofunc(1, 2);
        main: function void () {}"""
        expect = "Undeclared Function: nofunc"
        self.assertTrue(TestChecker.test(input, expect, 419))

    def test20(self):
        input = """a: float = 3.0;
        test: function void (c: integer, d: integer) {}
        b: integer = test(1, 2);
        main: function void () {}"""
        expect = "Type mismatch in expression: FuncCall(test, [IntegerLit(1), IntegerLit(2)])"
        self.assertTrue(TestChecker.test(input, expect, 420))

    def test21(self):
        input = """a: float = 3.0;
        test: function integer (c: integer, d: integer) {}
        b: integer = test(1);
        main: function void () {}"""
        expect = "Type mismatch in expression: FuncCall(test, [IntegerLit(1)])"
        self.assertTrue(TestChecker.test(input, expect, 421))

    def test22(self):
        input = """a: float = 3.0;
        test: function integer (c: integer, d: integer) {}
        b: integer = test(1, "string");
        main: function void () {}"""
        expect = "Type mismatch in expression: FuncCall(test, [IntegerLit(1), StringLit(string)])"
        self.assertTrue(TestChecker.test(input, expect, 422))

    def test23(self):
        input = """a: float = 3.0;
        voidfunc: function void () {}
        test: function integer (c: integer, d: integer) {
            voidfunc = 30;
        }
        b: integer = test(1, "string");
        main: function void () {}"""
        expect = "Type mismatch in statement: AssignStmt(Id(voidfunc), IntegerLit(30))"
        self.assertTrue(TestChecker.test(input, expect, 423))

    def test24(self):
        input = """a: float = 3.0;
        arr: array [2] of integer = {1,2};
        test: function integer (c: integer, d: integer) {
            arr = 30;
        }
        b: integer = test(1, "string");
        main: function void () {}"""
        expect = "Type mismatch in statement: AssignStmt(Id(arr), IntegerLit(30))"
        self.assertTrue(TestChecker.test(input, expect, 424))

    def test25(self):
        input = """a: float = 3.0;
        arr: array [2] of integer = {1,2};
        autoFunc: function auto () {}
        test: function integer (c: integer, d: integer) {
            a: auto = arr[0];
            a = autoFunc;
        }
        b: float = autoFunc;
        main: function void () {}"""
        expect = "Type mismatch in Variable Declaration: VarDecl(b, FloatType, Id(autoFunc))"
        self.assertTrue(TestChecker.test(input, expect, 425))

    def test26(self):
        input = """a: boolean = true;
        main: function void () {
            if (a + 1) {}
        }"""
        expect = "Type mismatch in expression: BinExpr(+, Id(a), IntegerLit(1))"
        self.assertTrue(TestChecker.test(input, expect, 426))

    def test27(self):
        input = """a: boolean = true;
        main: function void () {
            if ("string" :: "string") {}
        }"""
        expect = "Type mismatch in statement: IfStmt(BinExpr(::, StringLit(string), StringLit(string)), BlockStmt([]))"
        self.assertTrue(TestChecker.test(input, expect, 427))

    def test28(self):
        input = """a: boolean = true;
        main: function void () {
            if (a) {
                break;
            }
        }"""
        expect = "Must in loop: BreakStmt()"
        self.assertTrue(TestChecker.test(input, expect, 428))

    def test29(self):
        input = """a: boolean = true;
        main: function void () {
            if (a) {
                continue;
            }
        }"""
        expect = "Must in loop: ContinueStmt()"
        self.assertTrue(TestChecker.test(input, expect, 429))
