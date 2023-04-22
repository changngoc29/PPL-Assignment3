import unittest
from TestUtils import TestChecker
from AST import *


class CheckerSuite(unittest.TestCase):
    # def test0(self):
    #     input = """a: integer;
    #     c: float;
    #     a: float;"""
    #     expect = "Redeclared Variable: a"
    #     self.assertTrue(TestChecker.test(input, expect, 400))

    # def test1(self):
    #     input = """a: integer;
    #     c: float;"""
    #     expect = "No entry point"
    #     self.assertTrue(TestChecker.test(input, expect, 401))

    # def test2(self):
    #     input = """a: integer = 4;
    #     c: float;
    #     main: function void () {}
    #     a: string;"""
    #     expect = "Redeclared Variable: a"
    #     self.assertTrue(TestChecker.test(input, expect, 402))

    # def test3(self):
    #     input = """a: integer = 4;
    #     c: auto;
    #     main: function void () {}"""
    #     expect = "Invalid Variable: c"
    #     self.assertTrue(TestChecker.test(input, expect, 403))

    # def test4(self):
    #     input = """a: array [3] of integer = {1,2};
    #     main: function void () {}"""
    #     expect = "Type mismatch in Variable Declaration: VarDecl(a, ArrayType([3], IntegerType), ArrayLit([IntegerLit(1), IntegerLit(2)]))"
    #     self.assertTrue(TestChecker.test(input, expect, 404))

    # def test5(self):
    #     input = """a: array [2] of float = {1.0 , "string"};
    #     main: function void () {}"""
    #     expect = "Illegal array literal: ArrayLit([FloatLit(1.0), StringLit(string)])"
    #     self.assertTrue(TestChecker.test(input, expect, 405))

    # def test6(self):
    #     input = """a: array [2] of float = {"string", "string"};
    #     main: function void () {}"""
    #     expect = "Type mismatch in Variable Declaration: VarDecl(a, ArrayType([2], FloatType), ArrayLit([StringLit(string), StringLit(string)]))"
    #     self.assertTrue(TestChecker.test(input, expect, 406))

    # def test7(self):
    #     input = """a: integer = 2 + 3;
    #     b: float = a + 3.2;
    #     c: integer = b;
    #     main: function void () {}"""
    #     expect = "Type mismatch in Variable Declaration: VarDecl(c, IntegerType, Id(b))"
    #     self.assertTrue(TestChecker.test(input, expect, 407))

    # def test8(self):
    #     input = """a: integer = 5 + 4;
    #     b: float = 3.0;
    #     q: boolean = true || false;
    #     c: integer = a % b;
    #     main: function void () {}"""
    #     expect = "Type mismatch in expression: BinExpr(%, Id(a), Id(b))"
    #     self.assertTrue(TestChecker.test(input, expect, 408))

    # def test9(self):
    #     input = """a: integer = 5 + 4;
    #     b: float = 3.0;
    #     c: string = "string" :: "string";
    #     g: boolean = 1 < 3.0;
    #     q: boolean = true && 1;
    #     main: function void () {}"""
    #     expect = (
    #         "Type mismatch in expression: BinExpr(&&, BooleanLit(True), IntegerLit(1))"
    #     )
    #     self.assertTrue(TestChecker.test(input, expect, 409))

    # def test10(self):
    #     input = """a: array [2, 3] of integer = {{1, 2, 3}, {1, 3, 4}};
    #     c: array [3] of integer = a[1];
    #     b: array [1, 3] of integer = {{1, 2, 3}, {1, 3, 4}};
    #     main: function void () {}"""
    #     expect = "Type mismatch in Variable Declaration: VarDecl(b, ArrayType([1, 3], IntegerType), ArrayLit([ArrayLit([IntegerLit(1), IntegerLit(2), IntegerLit(3)]), ArrayLit([IntegerLit(1), IntegerLit(3), IntegerLit(4)])]))"
    #     self.assertTrue(TestChecker.test(input, expect, 410))

    # def test11(self):
    #     input = """a: array [2,2] of integer = {{1, 2}, {"string", "string"}};
    #     main: function void () {}"""
    #     expect = "Illegal array literal: ArrayLit([ArrayLit([IntegerLit(1), IntegerLit(2)]), ArrayLit([StringLit(string), StringLit(string)])])"
    #     self.assertTrue(TestChecker.test(input, expect, 411))

    # def test12(self):
    #     input = """a: array [2,2] of integer = {{1, 2, 3}, {1, 2}};
    #     main: function void () {}"""
    #     expect = "Illegal array literal: ArrayLit([ArrayLit([IntegerLit(1), IntegerLit(2), IntegerLit(3)]), ArrayLit([IntegerLit(1), IntegerLit(2)])])"
    #     self.assertTrue(TestChecker.test(input, expect, 412))

    # def test13(self):
    #     input = """a: array [2,2] of integer = {{2, 3}, {1, 2}};
    #     b: integer = c[0];
    #     main: function void () {}"""
    #     expect = "Undeclared Identifier: c"
    #     self.assertTrue(TestChecker.test(input, expect, 413))

    # def test14(self):
    #     input = """a: array [2,2] of integer = {{2, 3}, {1, 2}};
    #     b: integer = 20;
    #     c: integer = b[1];
    #     main: function void () {}"""
    #     expect = "Type mismatch in expression: ArrayCell(b, [IntegerLit(1)])"
    #     self.assertTrue(TestChecker.test(input, expect, 414))

    # def test15(self):
    #     input = """a: array [2] of integer = {1, 2};
    #     b: integer = a[1, 2];
    #     main: function void () {}"""
    #     expect = (
    #         "Type mismatch in expression: ArrayCell(a, [IntegerLit(1), IntegerLit(2)])"
    #     )
    #     self.assertTrue(TestChecker.test(input, expect, 415))

    # def test16(self):
    #     input = """a: array [2] of integer = {1, 2};
    #     b: integer = a["string"];
    #     main: function void () {}"""
    #     expect = "Type mismatch in expression: ArrayCell(a, [StringLit(string)])"
    #     self.assertTrue(TestChecker.test(input, expect, 416))

    # def test17(self):
    #     input = """a: array [2] of integer = {1, 2};
    #     b: float = a[1];
    #     g: auto;
    #     main: function void () {}"""
    #     expect = "Invalid Variable: g"
    #     self.assertTrue(TestChecker.test(input, expect, 417))

    # def test18(self):
    #     input = """a: array [2, 2, 1] of integer = {{{1},{3}}, {{1},{4}}};
    #     c: array [2, 1] of integer = a[0];
    #     b: float = a[1,1,1];
    #     c: auto = 4;
    #     main: function void () {}"""
    #     expect = "Redeclared Variable: c"
    #     self.assertTrue(TestChecker.test(input, expect, 418))

    # def test19(self):
    #     input = """a: float = 3.0;
    #     test: function integer (c: integer, d: integer) {}
    #     b: integer = nofunc(1, 2);
    #     main: function void () {}"""
    #     expect = "Undeclared Function: nofunc"
    #     self.assertTrue(TestChecker.test(input, expect, 419))

    # def test20(self):
    #     input = """a: float = 3.0;
    #     test: function void (c: integer, d: integer) {}
    #     b: integer = test(1, 2);
    #     main: function void () {}"""
    #     expect = "Type mismatch in expression: FuncCall(test, [IntegerLit(1), IntegerLit(2)])"
    #     self.assertTrue(TestChecker.test(input, expect, 420))

    # def test21(self):
    #     input = """a: float = 3.0;
    #     test: function integer (c: integer, d: integer) {}
    #     b: integer = test(1);
    #     main: function void () {}"""
    #     expect = "Type mismatch in expression: FuncCall(test, [IntegerLit(1)])"
    #     self.assertTrue(TestChecker.test(input, expect, 421))

    # def test22(self):
    #     input = """a: float = 3.0;
    #     test: function integer (c: integer, d: integer) {}
    #     b: integer = test(1, "string");
    #     main: function void () {}"""
    #     expect = "Type mismatch in expression: FuncCall(test, [IntegerLit(1), StringLit(string)])"
    #     self.assertTrue(TestChecker.test(input, expect, 422))

    # def test23(self):
    #     input = """a: float = 3.0;
    #     voidfunc: function void () {}
    #     test: function integer (c: integer, d: integer) {
    #         voidfunc = 30;
    #     }
    #     b: integer = test(1, "string");
    #     main: function void () {}"""
    #     expect = "Type mismatch in expression: Id(voidfunc)"
    #     self.assertTrue(TestChecker.test(input, expect, 423))

    # def test24(self):
    #     input = """a: float = 3.0;
    #     arr: array [2] of integer = {1,2};
    #     test: function integer (c: integer, d: integer) {
    #         arr = 30;
    #     }
    #     b: integer = test(1, "string");
    #     main: function void () {}"""
    #     expect = "Type mismatch in statement: AssignStmt(Id(arr), IntegerLit(30))"
    #     self.assertTrue(TestChecker.test(input, expect, 424))

    # def test25(self):
    #     input = """a: float = 3.0;
    #     arr: array [2] of integer = {1,2};
    #     autoFunc: function auto () {}
    #     test: function integer (c: integer, d: integer) {
    #         a: auto = arr[0];
    #         a = autoFunc();
    #     }
    #     b: string = autoFunc();
    #     main: function void () {}"""
    #     expect = "Type mismatch in Variable Declaration: VarDecl(b, StringType, FuncCall(autoFunc, []))"
    #     self.assertTrue(TestChecker.test(input, expect, 425))

    # def test26(self):
    #     input = """a: boolean = true;
    #     main: function void () {
    #         if (a + 1) {}
    #     }"""
    #     expect = "Type mismatch in expression: BinExpr(+, Id(a), IntegerLit(1))"
    #     self.assertTrue(TestChecker.test(input, expect, 426))

    # def test27(self):
    #     input = """a: boolean = true;
    #     main: function void () {
    #         if ("string" :: "string") {}
    #     }"""
    #     expect = "Type mismatch in statement: IfStmt(BinExpr(::, StringLit(string), StringLit(string)), BlockStmt([]))"
    #     self.assertTrue(TestChecker.test(input, expect, 427))

    # def test28(self):
    #     input = """a: boolean = true;
    #     main: function void () {
    #         if (a) {
    #             break;
    #         }
    #     }"""
    #     expect = "Must in loop: BreakStmt()"
    #     self.assertTrue(TestChecker.test(input, expect, 428))

    # def test29(self):
    #     input = """a: boolean = true;
    #     main: function void () {
    #         if (a) {
    #             continue;
    #         }
    #     }"""
    #     expect = "Must in loop: ContinueStmt()"
    #     self.assertTrue(TestChecker.test(input, expect, 429))

    # def test30(self):
    #     input = """a: boolean = true;
    #     main: function void () {
    #         i: boolean;
    #         for (i=true, i && false, 5) {}
    #     }"""
    #     expect = "Type mismatch in statement: ForStmt(AssignStmt(Id(i), BooleanLit(True)), BinExpr(&&, Id(i), BooleanLit(False)), IntegerLit(5), BlockStmt([]))"
    #     self.assertTrue(TestChecker.test(input, expect, 430))

    # def test31(self):
    #     input = """a: boolean = true;
    #     main: function void () {
    #         i: boolean;
    #         a: integer;
    #         for (a=1, a + 2, 5) {}
    #     }"""
    #     expect = "Type mismatch in statement: ForStmt(AssignStmt(Id(a), IntegerLit(1)), BinExpr(+, Id(a), IntegerLit(2)), IntegerLit(5), BlockStmt([]))"
    #     self.assertTrue(TestChecker.test(input, expect, 431))

    # def test32(self):
    #     input = """a: boolean = true;
    #     main: function void () {
    #         i: boolean;
    #         a: integer;
    #         for (a=1, a < 2, "string") {}
    #     }"""
    #     expect = "Type mismatch in statement: ForStmt(AssignStmt(Id(a), IntegerLit(1)), BinExpr(<, Id(a), IntegerLit(2)), StringLit(string), BlockStmt([]))"
    #     self.assertTrue(TestChecker.test(input, expect, 432))

    # def test33(self):
    #     input = """a: boolean = true;
    #     main: function void () {
    #         i: boolean;
    #         a: integer;
    #         for (a=1, a < 2, 5) {}
    #         g: auto;
    #     }"""
    #     expect = "Invalid Variable: g"
    #     self.assertTrue(TestChecker.test(input, expect, 433))

    # def test34(self):
    #     input = """a: boolean = true;
    #     main: function void () {
    #         i: boolean;
    #         a: integer = 4;
    #         while (a + 4) {}
    #         g: auto;
    #     }"""
    #     expect = "Type mismatch in statement: WhileStmt(BinExpr(+, Id(a), IntegerLit(4)), BlockStmt([]))"
    #     self.assertTrue(TestChecker.test(input, expect, 434))

    # def test35(self):
    #     input = """a: boolean = true;
    #     main: function void () {
    #         i: boolean;
    #         a: integer = 4;
    #         while (a == 4) {}
    #         g: auto;
    #     }"""
    #     expect = "Invalid Variable: g"
    #     self.assertTrue(TestChecker.test(input, expect, 435))

    # def test36(self):
    #     input = """a: boolean = true;
    #     main: function void () {
    #         i: boolean;
    #         a: integer = 4;
    #         do {} while (a>4);
    #         do {} while (a+4);
    #         g: auto;
    #     }"""
    #     expect = "Type mismatch in statement: DoWhileStmt(BinExpr(+, Id(a), IntegerLit(4)), BlockStmt([]))"
    #     self.assertTrue(TestChecker.test(input, expect, 436))

    # def test37(self):
    #     input = """a: boolean = true;
    #     voidfunc: function void (a: integer, b: integer) {}
    #     main: function void () {
    #         i: boolean;
    #         a: integer = 4;
    #         do {} while (a>4);
    #         voidfunc(a, 4);
    #         voidfunc(a, b);
    #     }"""
    #     expect = "Undeclared Identifier: b"
    #     self.assertTrue(TestChecker.test(input, expect, 437))

    # def test38(self):
    #     input = """a: boolean = true;
    #     voidfunc: function void (a: integer, b: integer) {
    #         a: integer;
    #     }
    #     main: function void () {}
    #     """
    #     expect = "Redeclared Variable: a"
    #     self.assertTrue(TestChecker.test(input, expect, 438))

    # def test39(self):
    #     input = """a: boolean = true;
    #     voidfunc: function void (c: integer, b: integer) {
    #         a: integer = 5;
    #         c = a;
    #         b = "string";
    #     }
    #     main: function void () {}
    #     """
    #     expect = "Type mismatch in statement: AssignStmt(Id(b), StringLit(string))"
    #     self.assertTrue(TestChecker.test(input, expect, 439))

    # def test40(self):
    #     input = """a: boolean = true;
    #     voidfunc: function void (c: integer, b: integer) {
    #         a: integer = 5;
    #         c = a;
    #         for (a=5, a<4, a+2) {
    #             if (a!=4) a = 4;
    #             else {
    #                 a = 4;
    #                 break;
    #             }
    #         }
    #         continue;
    #     }
    #     main: function void () {}
    #     """
    #     expect = "Must in loop: ContinueStmt()"
    #     self.assertTrue(TestChecker.test(input, expect, 440))

    # def test41(self):
    #     input = """a: boolean = true;
    #     test: function auto () {}
    #     main: function void () {
    #         a: integer = 4;
    #         c: float;
    #         a = test();
    #     }
    #     c: string = test();
    #     """
    #     expect = "Type mismatch in Variable Declaration: VarDecl(c, StringType, FuncCall(test, []))"
    #     self.assertTrue(TestChecker.test(input, expect, 441))

    # def test42(self):
    #     input = """a: boolean = true;
    #     test: function auto () {}
    #     main: function void () {
    #         a: integer = 4;
    #         c: string;
    #         if (true) {
    #             for (a=4, a<5, a+4) {
    #                 c: integer = 4;
    #                 c = test();
    #                 if (c>a) break;
    #                 d: float = 3.0;
    #                 d = test();
    #                 d = c;
    #             }
    #         }
    #         break;
    #     }
    #     """
    #     expect = "Must in loop: BreakStmt()"
    #     self.assertTrue(TestChecker.test(input, expect, 442))

    # def test43(self):
    #     input = """a: boolean = true;
    #     test: function auto () {}
    #     main: function void () {
    #         a: integer = 4;
    #         c: string;
    #         if (true) {
    #             for (a=4, a<5, a+4) {
    #                 c: integer = 4;
    #                 c = test;
    #                 if (c>a) break;
    #                 d: float = 3.0;
    #                 d = test();
    #                 d = c;
    #             }
    #         }
    #         break;
    #     }
    #     """
    #     expect = "Type mismatch in expression: Id(test)"
    #     self.assertTrue(TestChecker.test(input, expect, 443))

    # def test44(self):
    #     input = """a: boolean = true;
    #     test: function auto (a: auto, b: integer) {}
    #     main: function void () {
    #         a: integer = 4;
    #         c: string;
    #         if (true) {
    #             for (a=4, a<5, a+4) {
    #                 c: integer = 4;
    #                 c = test(true, a);
    #                 if (c>a) break;
    #             }
    #         }
    #         z: integer = test(false, 5);
    #     }
    #     """
    #     expect = "Type mismatch in Variable Declaration: VarDecl(z, IntegerType, FuncCall(test, [BooleanLit(False), IntegerLit(5)]))"
    #     self.assertTrue(TestChecker.test(input, expect, 444))

    # def test45(self):
    #     input = """a: boolean = true;
    #     test: function auto (a: auto, b: integer) {}
    #     main: function void () {
    #         a: integer = 4;
    #         c: string;
    #         if (true) {
    #             for (a=4, a<5, a+4) {
    #                 c: integer = 4;
    #                 c = test(true, a);
    #                 if (c>a) break;
    #             }
    #         }
    #         test(12.3, 5);
    #     }
    #     """
    #     expect = (
    #         "Type mismatch in statement: CallStmt(test, FloatLit(12.3), IntegerLit(5))"
    #     )
    #     self.assertTrue(TestChecker.test(input, expect, 445))

    def test46(self):
        input = """a: boolean = true;
        func0: function void (inherit a: integer, inherit b: integer) {} 
        func1: function auto (a: integer, c: integer) inherit func0 {}
        main: function void () {}
        """
        expect = "Invalid Parameter: a"
        self.assertTrue(TestChecker.test(input, expect, 446))
