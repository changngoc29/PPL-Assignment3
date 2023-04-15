# Generated from d:\222\PPL\assignment3-initial\src\main\mt22\parser\MT22.g4 by ANTLR 4.9.2
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
    from typing import TextIO
else:
    from typing.io import TextIO


from lexererr import *



def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2F")
        buf.write("\u024c\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7")
        buf.write("\t\7\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r")
        buf.write("\4\16\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23")
        buf.write("\t\23\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30")
        buf.write("\4\31\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36")
        buf.write("\t\36\4\37\t\37\4 \t \4!\t!\4\"\t\"\4#\t#\4$\t$\4%\t%")
        buf.write("\4&\t&\4\'\t\'\4(\t(\4)\t)\4*\t*\4+\t+\4,\t,\4-\t-\4.")
        buf.write("\t.\4/\t/\4\60\t\60\4\61\t\61\4\62\t\62\4\63\t\63\4\64")
        buf.write("\t\64\4\65\t\65\4\66\t\66\4\67\t\67\48\t8\49\t9\4:\t:")
        buf.write("\4;\t;\4<\t<\4=\t=\4>\t>\4?\t?\4@\t@\4A\tA\4B\tB\4C\t")
        buf.write("C\4D\tD\4E\tE\4F\tF\4G\tG\4H\tH\4I\tI\4J\tJ\3\2\3\2\3")
        buf.write("\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\3\3\3\3\3\3\3")
        buf.write("\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\4\3\4\3\4\3\4\3")
        buf.write("\4\3\4\3\4\3\4\3\4\3\4\3\5\3\5\3\5\3\5\3\5\3\5\3\5\3\5")
        buf.write("\3\5\3\5\3\5\3\6\3\6\3\6\3\6\3\6\3\6\3\6\3\6\3\6\3\6\3")
        buf.write("\6\3\6\3\7\3\7\3\7\3\7\3\7\3\7\3\7\3\7\3\7\3\7\3\7\3\7")
        buf.write("\3\7\3\b\3\b\3\b\3\b\3\b\3\b\3\b\3\b\3\b\3\b\3\b\3\t\3")
        buf.write("\t\3\t\3\t\3\t\3\t\3\t\3\t\3\t\3\t\3\t\3\t\3\n\3\n\3\n")
        buf.write("\3\n\3\n\3\n\3\13\3\13\3\13\3\13\3\13\3\13\3\13\3\13\3")
        buf.write("\13\3\13\3\13\3\13\3\13\3\13\3\13\3\f\3\f\3\f\3\f\7\f")
        buf.write("\u010d\n\f\f\f\16\f\u0110\13\f\3\f\3\f\3\r\3\r\3\r\3\r")
        buf.write("\7\r\u0118\n\r\f\r\16\r\u011b\13\r\3\r\3\r\3\r\3\r\3\r")
        buf.write("\3\16\3\16\3\16\3\16\3\16\3\17\3\17\3\17\3\17\3\17\3\17")
        buf.write("\3\17\3\17\3\20\3\20\3\20\3\20\3\20\3\21\3\21\3\21\3\21")
        buf.write("\3\21\3\21\3\22\3\22\3\22\3\22\3\22\3\22\3\23\3\23\3\23")
        buf.write("\3\23\3\23\3\23\3\24\3\24\3\24\3\24\3\24\3\24\3\24\3\25")
        buf.write("\3\25\3\25\3\25\3\26\3\26\3\26\3\26\3\26\3\26\3\26\3\26")
        buf.write("\3\27\3\27\3\27\3\27\3\27\3\27\3\27\3\30\3\30\3\30\3\30")
        buf.write("\3\31\3\31\3\31\3\31\3\31\3\31\3\31\3\31\3\31\3\32\3\32")
        buf.write("\3\32\3\33\3\33\3\33\3\33\3\33\3\33\3\33\3\33\3\33\3\34")
        buf.write("\3\34\3\34\3\35\3\35\3\35\3\35\3\35\3\36\3\36\3\36\3\37")
        buf.write("\3\37\3\37\3\37\3\37\3\37\3 \3 \3 \3 \3 \3 \3 \3 \3!\3")
        buf.write("!\3\"\3\"\3#\3#\3$\3$\3%\3%\3&\3&\3&\3\'\3\'\3\'\3(\3")
        buf.write("(\3)\3)\3*\3*\3+\3+\3+\3,\3,\3,\3-\3-\3-\3.\3.\3.\3/\3")
        buf.write("/\3/\3\60\3\60\3\61\3\61\3\62\3\62\3\63\3\63\3\64\3\64")
        buf.write("\3\65\3\65\3\66\3\66\3\67\3\67\38\38\39\39\3:\3:\3;\3")
        buf.write(";\3;\5;\u01d0\n;\3;\7;\u01d3\n;\f;\16;\u01d6\13;\3;\5")
        buf.write(";\u01d9\n;\3<\3<\3<\3<\3<\3<\3<\3<\3<\3<\3<\3<\3<\5<\u01e8")
        buf.write("\n<\3<\3<\3=\3=\7=\u01ee\n=\f=\16=\u01f1\13=\3>\3>\3>")
        buf.write("\5>\u01f6\n>\3>\6>\u01f9\n>\r>\16>\u01fa\3?\3?\3?\3?\3")
        buf.write("?\3@\3@\3@\3@\3@\3@\3A\3A\7A\u020a\nA\fA\16A\u020d\13")
        buf.write("A\3A\3A\3A\3B\3B\3B\3C\3C\5C\u0217\nC\3D\3D\7D\u021b\n")
        buf.write("D\fD\16D\u021e\13D\3E\6E\u0221\nE\rE\16E\u0222\3E\3E\3")
        buf.write("F\3F\3F\5F\u022a\nF\3G\3G\7G\u022e\nG\fG\16G\u0231\13")
        buf.write("G\3G\3G\3H\3H\7H\u0237\nH\fH\16H\u023a\13H\3H\3H\3H\3")
        buf.write("H\3I\3I\7I\u0242\nI\fI\16I\u0245\13I\3I\3I\3I\3J\3J\3")
        buf.write("J\3\u0119\2K\3\3\5\4\7\5\t\6\13\7\r\b\17\t\21\n\23\13")
        buf.write("\25\f\27\r\31\16\33\17\35\20\37\21!\22#\23%\24\'\25)\26")
        buf.write("+\27-\30/\31\61\32\63\33\65\34\67\359\36;\37= ?!A\"C#")
        buf.write("E$G%I&K\'M(O)Q*S+U,W-Y.[/]\60_\61a\62c\63e\64g\65i\66")
        buf.write("k\67m8o9q:s;u<w=y\2{\2}>\177?\u0081@\u0083\2\u0085\2\u0087")
        buf.write("A\u0089B\u008b\2\u008dC\u008fD\u0091E\u0093F\3\2\r\4\2")
        buf.write("\f\f\17\17\3\2\63;\3\2\62;\4\2GGgg\n\2$$))^^ddhhppttv")
        buf.write("v\7\2\f\f\17\17$$))^^\5\2C\\aac|\6\2\62;C\\aac|\5\2\13")
        buf.write("\f\17\17\"\"\t\2$$^^ddhhppttvv\5\2ddpptt\2\u025a\2\3\3")
        buf.write("\2\2\2\2\5\3\2\2\2\2\7\3\2\2\2\2\t\3\2\2\2\2\13\3\2\2")
        buf.write("\2\2\r\3\2\2\2\2\17\3\2\2\2\2\21\3\2\2\2\2\23\3\2\2\2")
        buf.write("\2\25\3\2\2\2\2\27\3\2\2\2\2\31\3\2\2\2\2\33\3\2\2\2\2")
        buf.write("\35\3\2\2\2\2\37\3\2\2\2\2!\3\2\2\2\2#\3\2\2\2\2%\3\2")
        buf.write("\2\2\2\'\3\2\2\2\2)\3\2\2\2\2+\3\2\2\2\2-\3\2\2\2\2/\3")
        buf.write("\2\2\2\2\61\3\2\2\2\2\63\3\2\2\2\2\65\3\2\2\2\2\67\3\2")
        buf.write("\2\2\29\3\2\2\2\2;\3\2\2\2\2=\3\2\2\2\2?\3\2\2\2\2A\3")
        buf.write("\2\2\2\2C\3\2\2\2\2E\3\2\2\2\2G\3\2\2\2\2I\3\2\2\2\2K")
        buf.write("\3\2\2\2\2M\3\2\2\2\2O\3\2\2\2\2Q\3\2\2\2\2S\3\2\2\2\2")
        buf.write("U\3\2\2\2\2W\3\2\2\2\2Y\3\2\2\2\2[\3\2\2\2\2]\3\2\2\2")
        buf.write("\2_\3\2\2\2\2a\3\2\2\2\2c\3\2\2\2\2e\3\2\2\2\2g\3\2\2")
        buf.write("\2\2i\3\2\2\2\2k\3\2\2\2\2m\3\2\2\2\2o\3\2\2\2\2q\3\2")
        buf.write("\2\2\2s\3\2\2\2\2u\3\2\2\2\2w\3\2\2\2\2}\3\2\2\2\2\177")
        buf.write("\3\2\2\2\2\u0081\3\2\2\2\2\u0087\3\2\2\2\2\u0089\3\2\2")
        buf.write("\2\2\u008d\3\2\2\2\2\u008f\3\2\2\2\2\u0091\3\2\2\2\2\u0093")
        buf.write("\3\2\2\2\3\u0095\3\2\2\2\5\u00a1\3\2\2\2\7\u00ae\3\2\2")
        buf.write("\2\t\u00b8\3\2\2\2\13\u00c3\3\2\2\2\r\u00cf\3\2\2\2\17")
        buf.write("\u00dc\3\2\2\2\21\u00e7\3\2\2\2\23\u00f3\3\2\2\2\25\u00f9")
        buf.write("\3\2\2\2\27\u0108\3\2\2\2\31\u0113\3\2\2\2\33\u0121\3")
        buf.write("\2\2\2\35\u0126\3\2\2\2\37\u012e\3\2\2\2!\u0133\3\2\2")
        buf.write("\2#\u0139\3\2\2\2%\u013f\3\2\2\2\'\u0145\3\2\2\2)\u014c")
        buf.write("\3\2\2\2+\u0150\3\2\2\2-\u0158\3\2\2\2/\u015f\3\2\2\2")
        buf.write("\61\u0163\3\2\2\2\63\u016c\3\2\2\2\65\u016f\3\2\2\2\67")
        buf.write("\u0178\3\2\2\29\u017b\3\2\2\2;\u0180\3\2\2\2=\u0183\3")
        buf.write("\2\2\2?\u0189\3\2\2\2A\u0191\3\2\2\2C\u0193\3\2\2\2E\u0195")
        buf.write("\3\2\2\2G\u0197\3\2\2\2I\u0199\3\2\2\2K\u019b\3\2\2\2")
        buf.write("M\u019e\3\2\2\2O\u01a1\3\2\2\2Q\u01a3\3\2\2\2S\u01a5\3")
        buf.write("\2\2\2U\u01a7\3\2\2\2W\u01aa\3\2\2\2Y\u01ad\3\2\2\2[\u01b0")
        buf.write("\3\2\2\2]\u01b3\3\2\2\2_\u01b6\3\2\2\2a\u01b8\3\2\2\2")
        buf.write("c\u01ba\3\2\2\2e\u01bc\3\2\2\2g\u01be\3\2\2\2i\u01c0\3")
        buf.write("\2\2\2k\u01c2\3\2\2\2m\u01c4\3\2\2\2o\u01c6\3\2\2\2q\u01c8")
        buf.write("\3\2\2\2s\u01ca\3\2\2\2u\u01d8\3\2\2\2w\u01e7\3\2\2\2")
        buf.write("y\u01eb\3\2\2\2{\u01f2\3\2\2\2}\u01fc\3\2\2\2\177\u0201")
        buf.write("\3\2\2\2\u0081\u0207\3\2\2\2\u0083\u0211\3\2\2\2\u0085")
        buf.write("\u0216\3\2\2\2\u0087\u0218\3\2\2\2\u0089\u0220\3\2\2\2")
        buf.write("\u008b\u0229\3\2\2\2\u008d\u022b\3\2\2\2\u008f\u0234\3")
        buf.write("\2\2\2\u0091\u023f\3\2\2\2\u0093\u0249\3\2\2\2\u0095\u0096")
        buf.write("\7t\2\2\u0096\u0097\7g\2\2\u0097\u0098\7c\2\2\u0098\u0099")
        buf.write("\7f\2\2\u0099\u009a\7K\2\2\u009a\u009b\7p\2\2\u009b\u009c")
        buf.write("\7v\2\2\u009c\u009d\7g\2\2\u009d\u009e\7i\2\2\u009e\u009f")
        buf.write("\7g\2\2\u009f\u00a0\7t\2\2\u00a0\4\3\2\2\2\u00a1\u00a2")
        buf.write("\7r\2\2\u00a2\u00a3\7t\2\2\u00a3\u00a4\7k\2\2\u00a4\u00a5")
        buf.write("\7p\2\2\u00a5\u00a6\7v\2\2\u00a6\u00a7\7K\2\2\u00a7\u00a8")
        buf.write("\7p\2\2\u00a8\u00a9\7v\2\2\u00a9\u00aa\7g\2\2\u00aa\u00ab")
        buf.write("\7i\2\2\u00ab\u00ac\7g\2\2\u00ac\u00ad\7t\2\2\u00ad\6")
        buf.write("\3\2\2\2\u00ae\u00af\7t\2\2\u00af\u00b0\7g\2\2\u00b0\u00b1")
        buf.write("\7c\2\2\u00b1\u00b2\7f\2\2\u00b2\u00b3\7H\2\2\u00b3\u00b4")
        buf.write("\7n\2\2\u00b4\u00b5\7q\2\2\u00b5\u00b6\7c\2\2\u00b6\u00b7")
        buf.write("\7v\2\2\u00b7\b\3\2\2\2\u00b8\u00b9\7y\2\2\u00b9\u00ba")
        buf.write("\7t\2\2\u00ba\u00bb\7k\2\2\u00bb\u00bc\7v\2\2\u00bc\u00bd")
        buf.write("\7g\2\2\u00bd\u00be\7H\2\2\u00be\u00bf\7n\2\2\u00bf\u00c0")
        buf.write("\7q\2\2\u00c0\u00c1\7c\2\2\u00c1\u00c2\7v\2\2\u00c2\n")
        buf.write("\3\2\2\2\u00c3\u00c4\7t\2\2\u00c4\u00c5\7g\2\2\u00c5\u00c6")
        buf.write("\7c\2\2\u00c6\u00c7\7f\2\2\u00c7\u00c8\7D\2\2\u00c8\u00c9")
        buf.write("\7q\2\2\u00c9\u00ca\7q\2\2\u00ca\u00cb\7n\2\2\u00cb\u00cc")
        buf.write("\7g\2\2\u00cc\u00cd\7c\2\2\u00cd\u00ce\7p\2\2\u00ce\f")
        buf.write("\3\2\2\2\u00cf\u00d0\7r\2\2\u00d0\u00d1\7t\2\2\u00d1\u00d2")
        buf.write("\7k\2\2\u00d2\u00d3\7p\2\2\u00d3\u00d4\7v\2\2\u00d4\u00d5")
        buf.write("\7D\2\2\u00d5\u00d6\7q\2\2\u00d6\u00d7\7q\2\2\u00d7\u00d8")
        buf.write("\7n\2\2\u00d8\u00d9\7g\2\2\u00d9\u00da\7c\2\2\u00da\u00db")
        buf.write("\7p\2\2\u00db\16\3\2\2\2\u00dc\u00dd\7t\2\2\u00dd\u00de")
        buf.write("\7g\2\2\u00de\u00df\7c\2\2\u00df\u00e0\7f\2\2\u00e0\u00e1")
        buf.write("\7U\2\2\u00e1\u00e2\7v\2\2\u00e2\u00e3\7t\2\2\u00e3\u00e4")
        buf.write("\7k\2\2\u00e4\u00e5\7p\2\2\u00e5\u00e6\7i\2\2\u00e6\20")
        buf.write("\3\2\2\2\u00e7\u00e8\7r\2\2\u00e8\u00e9\7t\2\2\u00e9\u00ea")
        buf.write("\7k\2\2\u00ea\u00eb\7p\2\2\u00eb\u00ec\7v\2\2\u00ec\u00ed")
        buf.write("\7U\2\2\u00ed\u00ee\7v\2\2\u00ee\u00ef\7t\2\2\u00ef\u00f0")
        buf.write("\7k\2\2\u00f0\u00f1\7p\2\2\u00f1\u00f2\7i\2\2\u00f2\22")
        buf.write("\3\2\2\2\u00f3\u00f4\7u\2\2\u00f4\u00f5\7w\2\2\u00f5\u00f6")
        buf.write("\7r\2\2\u00f6\u00f7\7g\2\2\u00f7\u00f8\7t\2\2\u00f8\24")
        buf.write("\3\2\2\2\u00f9\u00fa\7r\2\2\u00fa\u00fb\7t\2\2\u00fb\u00fc")
        buf.write("\7g\2\2\u00fc\u00fd\7x\2\2\u00fd\u00fe\7g\2\2\u00fe\u00ff")
        buf.write("\7p\2\2\u00ff\u0100\7v\2\2\u0100\u0101\7F\2\2\u0101\u0102")
        buf.write("\7g\2\2\u0102\u0103\7h\2\2\u0103\u0104\7c\2\2\u0104\u0105")
        buf.write("\7w\2\2\u0105\u0106\7n\2\2\u0106\u0107\7v\2\2\u0107\26")
        buf.write("\3\2\2\2\u0108\u0109\7\61\2\2\u0109\u010a\7\61\2\2\u010a")
        buf.write("\u010e\3\2\2\2\u010b\u010d\n\2\2\2\u010c\u010b\3\2\2\2")
        buf.write("\u010d\u0110\3\2\2\2\u010e\u010c\3\2\2\2\u010e\u010f\3")
        buf.write("\2\2\2\u010f\u0111\3\2\2\2\u0110\u010e\3\2\2\2\u0111\u0112")
        buf.write("\b\f\2\2\u0112\30\3\2\2\2\u0113\u0114\7\61\2\2\u0114\u0115")
        buf.write("\7,\2\2\u0115\u0119\3\2\2\2\u0116\u0118\13\2\2\2\u0117")
        buf.write("\u0116\3\2\2\2\u0118\u011b\3\2\2\2\u0119\u011a\3\2\2\2")
        buf.write("\u0119\u0117\3\2\2\2\u011a\u011c\3\2\2\2\u011b\u0119\3")
        buf.write("\2\2\2\u011c\u011d\7,\2\2\u011d\u011e\7\61\2\2\u011e\u011f")
        buf.write("\3\2\2\2\u011f\u0120\b\r\2\2\u0120\32\3\2\2\2\u0121\u0122")
        buf.write("\7c\2\2\u0122\u0123\7w\2\2\u0123\u0124\7v\2\2\u0124\u0125")
        buf.write("\7q\2\2\u0125\34\3\2\2\2\u0126\u0127\7k\2\2\u0127\u0128")
        buf.write("\7p\2\2\u0128\u0129\7v\2\2\u0129\u012a\7g\2\2\u012a\u012b")
        buf.write("\7i\2\2\u012b\u012c\7g\2\2\u012c\u012d\7t\2\2\u012d\36")
        buf.write("\3\2\2\2\u012e\u012f\7x\2\2\u012f\u0130\7q\2\2\u0130\u0131")
        buf.write("\7k\2\2\u0131\u0132\7f\2\2\u0132 \3\2\2\2\u0133\u0134")
        buf.write("\7c\2\2\u0134\u0135\7t\2\2\u0135\u0136\7t\2\2\u0136\u0137")
        buf.write("\7c\2\2\u0137\u0138\7{\2\2\u0138\"\3\2\2\2\u0139\u013a")
        buf.write("\7d\2\2\u013a\u013b\7t\2\2\u013b\u013c\7g\2\2\u013c\u013d")
        buf.write("\7c\2\2\u013d\u013e\7m\2\2\u013e$\3\2\2\2\u013f\u0140")
        buf.write("\7h\2\2\u0140\u0141\7n\2\2\u0141\u0142\7q\2\2\u0142\u0143")
        buf.write("\7c\2\2\u0143\u0144\7v\2\2\u0144&\3\2\2\2\u0145\u0146")
        buf.write("\7t\2\2\u0146\u0147\7g\2\2\u0147\u0148\7v\2\2\u0148\u0149")
        buf.write("\7w\2\2\u0149\u014a\7t\2\2\u014a\u014b\7p\2\2\u014b(\3")
        buf.write("\2\2\2\u014c\u014d\7q\2\2\u014d\u014e\7w\2\2\u014e\u014f")
        buf.write("\7v\2\2\u014f*\3\2\2\2\u0150\u0151\7d\2\2\u0151\u0152")
        buf.write("\7q\2\2\u0152\u0153\7q\2\2\u0153\u0154\7n\2\2\u0154\u0155")
        buf.write("\7g\2\2\u0155\u0156\7c\2\2\u0156\u0157\7p\2\2\u0157,\3")
        buf.write("\2\2\2\u0158\u0159\7u\2\2\u0159\u015a\7v\2\2\u015a\u015b")
        buf.write("\7t\2\2\u015b\u015c\7k\2\2\u015c\u015d\7p\2\2\u015d\u015e")
        buf.write("\7i\2\2\u015e.\3\2\2\2\u015f\u0160\7h\2\2\u0160\u0161")
        buf.write("\7q\2\2\u0161\u0162\7t\2\2\u0162\60\3\2\2\2\u0163\u0164")
        buf.write("\7e\2\2\u0164\u0165\7q\2\2\u0165\u0166\7p\2\2\u0166\u0167")
        buf.write("\7v\2\2\u0167\u0168\7k\2\2\u0168\u0169\7p\2\2\u0169\u016a")
        buf.write("\7w\2\2\u016a\u016b\7g\2\2\u016b\62\3\2\2\2\u016c\u016d")
        buf.write("\7f\2\2\u016d\u016e\7q\2\2\u016e\64\3\2\2\2\u016f\u0170")
        buf.write("\7h\2\2\u0170\u0171\7w\2\2\u0171\u0172\7p\2\2\u0172\u0173")
        buf.write("\7e\2\2\u0173\u0174\7v\2\2\u0174\u0175\7k\2\2\u0175\u0176")
        buf.write("\7q\2\2\u0176\u0177\7p\2\2\u0177\66\3\2\2\2\u0178\u0179")
        buf.write("\7q\2\2\u0179\u017a\7h\2\2\u017a8\3\2\2\2\u017b\u017c")
        buf.write("\7g\2\2\u017c\u017d\7n\2\2\u017d\u017e\7u\2\2\u017e\u017f")
        buf.write("\7g\2\2\u017f:\3\2\2\2\u0180\u0181\7k\2\2\u0181\u0182")
        buf.write("\7h\2\2\u0182<\3\2\2\2\u0183\u0184\7y\2\2\u0184\u0185")
        buf.write("\7j\2\2\u0185\u0186\7k\2\2\u0186\u0187\7n\2\2\u0187\u0188")
        buf.write("\7g\2\2\u0188>\3\2\2\2\u0189\u018a\7k\2\2\u018a\u018b")
        buf.write("\7p\2\2\u018b\u018c\7j\2\2\u018c\u018d\7g\2\2\u018d\u018e")
        buf.write("\7t\2\2\u018e\u018f\7k\2\2\u018f\u0190\7v\2\2\u0190@\3")
        buf.write("\2\2\2\u0191\u0192\7-\2\2\u0192B\3\2\2\2\u0193\u0194\7")
        buf.write("/\2\2\u0194D\3\2\2\2\u0195\u0196\7,\2\2\u0196F\3\2\2\2")
        buf.write("\u0197\u0198\7\61\2\2\u0198H\3\2\2\2\u0199\u019a\7\'\2")
        buf.write("\2\u019aJ\3\2\2\2\u019b\u019c\7(\2\2\u019c\u019d\7(\2")
        buf.write("\2\u019dL\3\2\2\2\u019e\u019f\7~\2\2\u019f\u01a0\7~\2")
        buf.write("\2\u01a0N\3\2\2\2\u01a1\u01a2\7#\2\2\u01a2P\3\2\2\2\u01a3")
        buf.write("\u01a4\7@\2\2\u01a4R\3\2\2\2\u01a5\u01a6\7>\2\2\u01a6")
        buf.write("T\3\2\2\2\u01a7\u01a8\7@\2\2\u01a8\u01a9\7?\2\2\u01a9")
        buf.write("V\3\2\2\2\u01aa\u01ab\7>\2\2\u01ab\u01ac\7?\2\2\u01ac")
        buf.write("X\3\2\2\2\u01ad\u01ae\7?\2\2\u01ae\u01af\7?\2\2\u01af")
        buf.write("Z\3\2\2\2\u01b0\u01b1\7#\2\2\u01b1\u01b2\7?\2\2\u01b2")
        buf.write("\\\3\2\2\2\u01b3\u01b4\7<\2\2\u01b4\u01b5\7<\2\2\u01b5")
        buf.write("^\3\2\2\2\u01b6\u01b7\7=\2\2\u01b7`\3\2\2\2\u01b8\u01b9")
        buf.write("\7<\2\2\u01b9b\3\2\2\2\u01ba\u01bb\7?\2\2\u01bbd\3\2\2")
        buf.write("\2\u01bc\u01bd\7.\2\2\u01bdf\3\2\2\2\u01be\u01bf\7\60")
        buf.write("\2\2\u01bfh\3\2\2\2\u01c0\u01c1\7*\2\2\u01c1j\3\2\2\2")
        buf.write("\u01c2\u01c3\7+\2\2\u01c3l\3\2\2\2\u01c4\u01c5\7]\2\2")
        buf.write("\u01c5n\3\2\2\2\u01c6\u01c7\7_\2\2\u01c7p\3\2\2\2\u01c8")
        buf.write("\u01c9\7}\2\2\u01c9r\3\2\2\2\u01ca\u01cb\7\177\2\2\u01cb")
        buf.write("t\3\2\2\2\u01cc\u01d9\7\62\2\2\u01cd\u01d4\t\3\2\2\u01ce")
        buf.write("\u01d0\7a\2\2\u01cf\u01ce\3\2\2\2\u01cf\u01d0\3\2\2\2")
        buf.write("\u01d0\u01d1\3\2\2\2\u01d1\u01d3\t\4\2\2\u01d2\u01cf\3")
        buf.write("\2\2\2\u01d3\u01d6\3\2\2\2\u01d4\u01d2\3\2\2\2\u01d4\u01d5")
        buf.write("\3\2\2\2\u01d5\u01d7\3\2\2\2\u01d6\u01d4\3\2\2\2\u01d7")
        buf.write("\u01d9\b;\3\2\u01d8\u01cc\3\2\2\2\u01d8\u01cd\3\2\2\2")
        buf.write("\u01d9v\3\2\2\2\u01da\u01db\5u;\2\u01db\u01dc\5y=\2\u01dc")
        buf.write("\u01dd\5{>\2\u01dd\u01e8\3\2\2\2\u01de\u01df\5u;\2\u01df")
        buf.write("\u01e0\5y=\2\u01e0\u01e8\3\2\2\2\u01e1\u01e2\5u;\2\u01e2")
        buf.write("\u01e3\5{>\2\u01e3\u01e8\3\2\2\2\u01e4\u01e5\5y=\2\u01e5")
        buf.write("\u01e6\5{>\2\u01e6\u01e8\3\2\2\2\u01e7\u01da\3\2\2\2\u01e7")
        buf.write("\u01de\3\2\2\2\u01e7\u01e1\3\2\2\2\u01e7\u01e4\3\2\2\2")
        buf.write("\u01e8\u01e9\3\2\2\2\u01e9\u01ea\b<\4\2\u01eax\3\2\2\2")
        buf.write("\u01eb\u01ef\5g\64\2\u01ec\u01ee\t\4\2\2\u01ed\u01ec\3")
        buf.write("\2\2\2\u01ee\u01f1\3\2\2\2\u01ef\u01ed\3\2\2\2\u01ef\u01f0")
        buf.write("\3\2\2\2\u01f0z\3\2\2\2\u01f1\u01ef\3\2\2\2\u01f2\u01f5")
        buf.write("\t\5\2\2\u01f3\u01f6\5A!\2\u01f4\u01f6\5C\"\2\u01f5\u01f3")
        buf.write("\3\2\2\2\u01f5\u01f4\3\2\2\2\u01f5\u01f6\3\2\2\2\u01f6")
        buf.write("\u01f8\3\2\2\2\u01f7\u01f9\t\4\2\2\u01f8\u01f7\3\2\2\2")
        buf.write("\u01f9\u01fa\3\2\2\2\u01fa\u01f8\3\2\2\2\u01fa\u01fb\3")
        buf.write("\2\2\2\u01fb|\3\2\2\2\u01fc\u01fd\7v\2\2\u01fd\u01fe\7")
        buf.write("t\2\2\u01fe\u01ff\7w\2\2\u01ff\u0200\7g\2\2\u0200~\3\2")
        buf.write("\2\2\u0201\u0202\7h\2\2\u0202\u0203\7c\2\2\u0203\u0204")
        buf.write("\7n\2\2\u0204\u0205\7u\2\2\u0205\u0206\7g\2\2\u0206\u0080")
        buf.write("\3\2\2\2\u0207\u020b\7$\2\2\u0208\u020a\5\u0085C\2\u0209")
        buf.write("\u0208\3\2\2\2\u020a\u020d\3\2\2\2\u020b\u0209\3\2\2\2")
        buf.write("\u020b\u020c\3\2\2\2\u020c\u020e\3\2\2\2\u020d\u020b\3")
        buf.write("\2\2\2\u020e\u020f\7$\2\2\u020f\u0210\bA\5\2\u0210\u0082")
        buf.write("\3\2\2\2\u0211\u0212\7^\2\2\u0212\u0213\t\6\2\2\u0213")
        buf.write("\u0084\3\2\2\2\u0214\u0217\n\7\2\2\u0215\u0217\5\u0083")
        buf.write("B\2\u0216\u0214\3\2\2\2\u0216\u0215\3\2\2\2\u0217\u0086")
        buf.write("\3\2\2\2\u0218\u021c\t\b\2\2\u0219\u021b\t\t\2\2\u021a")
        buf.write("\u0219\3\2\2\2\u021b\u021e\3\2\2\2\u021c\u021a\3\2\2\2")
        buf.write("\u021c\u021d\3\2\2\2\u021d\u0088\3\2\2\2\u021e\u021c\3")
        buf.write("\2\2\2\u021f\u0221\t\n\2\2\u0220\u021f\3\2\2\2\u0221\u0222")
        buf.write("\3\2\2\2\u0222\u0220\3\2\2\2\u0222\u0223\3\2\2\2\u0223")
        buf.write("\u0224\3\2\2\2\u0224\u0225\bE\2\2\u0225\u008a\3\2\2\2")
        buf.write("\u0226\u0227\7^\2\2\u0227\u022a\n\13\2\2\u0228\u022a\7")
        buf.write("^\2\2\u0229\u0226\3\2\2\2\u0229\u0228\3\2\2\2\u022a\u008c")
        buf.write("\3\2\2\2\u022b\u022f\7$\2\2\u022c\u022e\5\u0085C\2\u022d")
        buf.write("\u022c\3\2\2\2\u022e\u0231\3\2\2\2\u022f\u022d\3\2\2\2")
        buf.write("\u022f\u0230\3\2\2\2\u0230\u0232\3\2\2\2\u0231\u022f\3")
        buf.write("\2\2\2\u0232\u0233\bG\6\2\u0233\u008e\3\2\2\2\u0234\u0238")
        buf.write("\7$\2\2\u0235\u0237\5\u0085C\2\u0236\u0235\3\2\2\2\u0237")
        buf.write("\u023a\3\2\2\2\u0238\u0236\3\2\2\2\u0238\u0239\3\2\2\2")
        buf.write("\u0239\u023b\3\2\2\2\u023a\u0238\3\2\2\2\u023b\u023c\7")
        buf.write("^\2\2\u023c\u023d\t\f\2\2\u023d\u023e\bH\7\2\u023e\u0090")
        buf.write("\3\2\2\2\u023f\u0243\7$\2\2\u0240\u0242\5\u0085C\2\u0241")
        buf.write("\u0240\3\2\2\2\u0242\u0245\3\2\2\2\u0243\u0241\3\2\2\2")
        buf.write("\u0243\u0244\3\2\2\2\u0244\u0246\3\2\2\2\u0245\u0243\3")
        buf.write("\2\2\2\u0246\u0247\5\u008bF\2\u0247\u0248\bI\b\2\u0248")
        buf.write("\u0092\3\2\2\2\u0249\u024a\13\2\2\2\u024a\u024b\bJ\t\2")
        buf.write("\u024b\u0094\3\2\2\2\24\2\u010e\u0119\u01cf\u01d4\u01d8")
        buf.write("\u01e7\u01ef\u01f5\u01fa\u020b\u0216\u021c\u0222\u0229")
        buf.write("\u022f\u0238\u0243\n\b\2\2\3;\2\3<\3\3A\4\3G\5\3H\6\3")
        buf.write("I\7\3J\b")
        return buf.getvalue()


class MT22Lexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    T__0 = 1
    T__1 = 2
    T__2 = 3
    T__3 = 4
    T__4 = 5
    T__5 = 6
    T__6 = 7
    T__7 = 8
    T__8 = 9
    T__9 = 10
    LINE_COMMENT = 11
    LINES_COMMENT = 12
    AUTO = 13
    INT = 14
    VOID = 15
    ARRAY = 16
    BREAK = 17
    FLOAT = 18
    RETURN = 19
    OUT = 20
    BOOLEAN = 21
    STRING = 22
    FOR = 23
    CONTINUE = 24
    DO = 25
    FUNCTION = 26
    OF = 27
    ELSE = 28
    IF = 29
    WHILE = 30
    INHERIT = 31
    ADDOP = 32
    SUBOP = 33
    MULOP = 34
    DIVOP = 35
    MODOP = 36
    ANDOP = 37
    OROP = 38
    NOTOP = 39
    GTOP = 40
    SMOP = 41
    GTEOP = 42
    SMEOP = 43
    EQCOP = 44
    NOTEQOP = 45
    CONCATOP = 46
    SM = 47
    COLON = 48
    EQ = 49
    CM = 50
    DOT = 51
    LB = 52
    RB = 53
    LS = 54
    RS = 55
    LP = 56
    RP = 57
    INTLIT = 58
    FLOATLIT = 59
    TRUE = 60
    FALSE = 61
    STRINGLIT = 62
    ID = 63
    WS = 64
    UNCLOSE_STRING_1 = 65
    UNCLOSE_STRING_2 = 66
    ILLEGAL_ESCAPE = 67
    ERROR_CHAR = 68

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'readInteger'", "'printInteger'", "'readFloat'", "'writeFloat'", 
            "'readBoolean'", "'printBoolean'", "'readString'", "'printString'", 
            "'super'", "'preventDefault'", "'auto'", "'integer'", "'void'", 
            "'array'", "'break'", "'float'", "'return'", "'out'", "'boolean'", 
            "'string'", "'for'", "'continue'", "'do'", "'function'", "'of'", 
            "'else'", "'if'", "'while'", "'inherit'", "'+'", "'-'", "'*'", 
            "'/'", "'%'", "'&&'", "'||'", "'!'", "'>'", "'<'", "'>='", "'<='", 
            "'=='", "'!='", "'::'", "';'", "':'", "'='", "','", "'.'", "'('", 
            "')'", "'['", "']'", "'{'", "'}'", "'true'", "'false'" ]

    symbolicNames = [ "<INVALID>",
            "LINE_COMMENT", "LINES_COMMENT", "AUTO", "INT", "VOID", "ARRAY", 
            "BREAK", "FLOAT", "RETURN", "OUT", "BOOLEAN", "STRING", "FOR", 
            "CONTINUE", "DO", "FUNCTION", "OF", "ELSE", "IF", "WHILE", "INHERIT", 
            "ADDOP", "SUBOP", "MULOP", "DIVOP", "MODOP", "ANDOP", "OROP", 
            "NOTOP", "GTOP", "SMOP", "GTEOP", "SMEOP", "EQCOP", "NOTEQOP", 
            "CONCATOP", "SM", "COLON", "EQ", "CM", "DOT", "LB", "RB", "LS", 
            "RS", "LP", "RP", "INTLIT", "FLOATLIT", "TRUE", "FALSE", "STRINGLIT", 
            "ID", "WS", "UNCLOSE_STRING_1", "UNCLOSE_STRING_2", "ILLEGAL_ESCAPE", 
            "ERROR_CHAR" ]

    ruleNames = [ "T__0", "T__1", "T__2", "T__3", "T__4", "T__5", "T__6", 
                  "T__7", "T__8", "T__9", "LINE_COMMENT", "LINES_COMMENT", 
                  "AUTO", "INT", "VOID", "ARRAY", "BREAK", "FLOAT", "RETURN", 
                  "OUT", "BOOLEAN", "STRING", "FOR", "CONTINUE", "DO", "FUNCTION", 
                  "OF", "ELSE", "IF", "WHILE", "INHERIT", "ADDOP", "SUBOP", 
                  "MULOP", "DIVOP", "MODOP", "ANDOP", "OROP", "NOTOP", "GTOP", 
                  "SMOP", "GTEOP", "SMEOP", "EQCOP", "NOTEQOP", "CONCATOP", 
                  "SM", "COLON", "EQ", "CM", "DOT", "LB", "RB", "LS", "RS", 
                  "LP", "RP", "INTLIT", "FLOATLIT", "DECPART", "EXPPART", 
                  "TRUE", "FALSE", "STRINGLIT", "ESCAPE", "CHAR", "ID", 
                  "WS", "ESCAPE_ILLEGAL", "UNCLOSE_STRING_1", "UNCLOSE_STRING_2", 
                  "ILLEGAL_ESCAPE", "ERROR_CHAR" ]

    grammarFileName = "MT22.g4"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.9.2")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


    def action(self, localctx:RuleContext, ruleIndex:int, actionIndex:int):
        if self._actions is None:
            actions = dict()
            actions[57] = self.INTLIT_action 
            actions[58] = self.FLOATLIT_action 
            actions[63] = self.STRINGLIT_action 
            actions[69] = self.UNCLOSE_STRING_1_action 
            actions[70] = self.UNCLOSE_STRING_2_action 
            actions[71] = self.ILLEGAL_ESCAPE_action 
            actions[72] = self.ERROR_CHAR_action 
            self._actions = actions
        action = self._actions.get(ruleIndex, None)
        if action is not None:
            action(localctx, actionIndex)
        else:
            raise Exception("No registered action for:" + str(ruleIndex))


    def INTLIT_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 0:
            self.text = self.text.replace('_', '')
     

    def FLOATLIT_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 1:
            self.text = self.text.replace('_', '')
     

    def STRINGLIT_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 2:
            self.text = self.text[1:-1]
     

    def UNCLOSE_STRING_1_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 3:
            raise UncloseString(self.text[1:])
     

    def UNCLOSE_STRING_2_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 4:
            raise UncloseString(self.text[1:-1])
     

    def ILLEGAL_ESCAPE_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 5:
            raise IllegalEscape(self.text[1:])
     

    def ERROR_CHAR_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 6:
            raise ErrorToken(self.text)
     


