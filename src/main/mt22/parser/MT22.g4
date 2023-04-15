// 2053163
grammar MT22;

@lexer::header {
from lexererr import *
}

options{
	language=Python3;
}

program: decllist EOF ;

// DECLARATION
decllist: decl decllist | decl;
decl: vardecl | funcdecl;
vardecl: vardeclnoinit SM | vardeclinit SM;
vardeclnoinit: idlist COLON typ;
vardeclinit: ID CM vardeclinit CM expr | ID COLON typ EQ expr; 

funcdecl: ID COLON FUNCTION functyp LB paramlist RB (INHERIT ID)? blockstmt;
paramlist: params | ;
params: param CM params | param;
param: INHERIT? OUT? ID COLON typ;
functyp: typ | VOID ; 

// EXPRESSION
expr: relationalExpr CONCATOP relationalExpr | relationalExpr;

relationalExpr: logicalExpr relationalOpt logicalExpr | logicalExpr;
relationalOpt: EQCOP | NOTEQOP | SMOP | GTOP | SMEOP | GTEOP ;
logicalExpr: logicalExpr logicalOpt addExpr | addExpr;
logicalOpt: ANDOP | OROP;
addExpr: addExpr addOpt multiExpr | multiExpr;
addOpt: ADDOP | SUBOP;
multiExpr: multiExpr multiOpt unaryLogicalExpr | unaryLogicalExpr;
multiOpt: MULOP | DIVOP | MODOP;
unaryLogicalExpr: NOTOP unaryLogicalExpr | signExpr;
signExpr: SUBOP signExpr | indexOptExpr;
indexOptExpr: (ID LS nonullexprlist RS) | subexpr;
subexpr: ID 
	| alllit
	| LB expr RB
	| callexpr;
callexpr: (ID | specialFunc) LB nullexprlist RB;

// STATEMENTS
stmt: assignstmt | ifstmt | forstmt | whilestmt | dowhilestmt
	| breakstmt | continuestmt | returnstmt | callstmt
	| blockstmt;
assignstmt: scalarvar EQ expr SM;
ifstmt: IF LB expr RB stmt (ELSE stmt)? ;
forstmt: FOR LB scalarvar EQ expr CM expr CM expr RB stmt;
whilestmt: WHILE LB expr RB stmt;
dowhilestmt: DO blockstmt WHILE LB expr RB SM;
breakstmt: BREAK SM;
continuestmt: CONTINUE SM;
returnstmt: RETURN expr? SM;
callstmt: (ID | specialFunc) LB nullexprlist RB SM;
blockstmt: LP blockstmtbody RP;
blockstmtbody: declandstmts | ;
declandstmts: declandstmt declandstmts | declandstmt;
declandstmt: decl | stmt;
scalarvar: ID | (ID LS nonullexprlist RS);

// SMTMLIST & EXPRLIST
nonullexprlist: expr CM nonullexprlist | expr;
nullexprlist: nonullexprlist | ;

// IDLIST & TYP
idlist: ID CM idlist | ID;
typ: INT | FLOAT | STRING | BOOLEAN | AUTO | arraytyp;
arraytyp: ARRAY LS intList RS OF typ;
intList: intandexpr CM intList | intandexpr;
intandexpr: INTLIT | expr;
alllit: INTLIT | STRINGLIT | FLOATLIT | TRUE | FALSE | arrayLit;
arrayLit: LP arrayElements RP;
arrayElements: alllits | ; 
alllits: expr CM alllits | expr;

// SPECIAL FUNCTION
specialFunc: readInt | printInt | readFloat
	| writeFloat | readBoolean | printBoolean
	| readString | printString | superFunc | preventDefault;
readInt: 'readInteger';
printInt: 'printInteger';
readFloat: 'readFloat';
writeFloat: 'writeFloat';
readBoolean: 'readBoolean';
printBoolean: 'printBoolean';
readString: 'readString';
printString: 'printString';
superFunc: 'super';
preventDefault: 'preventDefault';

// COMMENT TOKENS
LINE_COMMENT : '//' ~[\r\n]* -> skip;
LINES_COMMENT : '/*' .*? '*/' -> skip;

// KEYWORD
AUTO: 'auto';
INT: 'integer';
VOID: 'void';
ARRAY: 'array';
BREAK: 'break';
FLOAT: 'float';
RETURN: 'return';
OUT: 'out';
BOOLEAN: 'boolean';
STRING: 'string';
FOR: 'for';
CONTINUE: 'continue';
DO: 'do';
FUNCTION: 'function';
OF: 'of';
ELSE: 'else';
IF: 'if';
WHILE: 'while';
INHERIT: 'inherit';

// OPERATOR
ADDOP: '+';
SUBOP: '-';
MULOP: '*';
DIVOP: '/';
MODOP: '%';
ANDOP: '&&';
OROP: '||';
NOTOP: '!';
GTOP: '>';
SMOP: '<';
GTEOP: '>=';
SMEOP: '<=';
EQCOP: '==';
NOTEQOP: '!=';
CONCATOP: '::';

// SEPARATE
SM: ';';
COLON: ':';
EQ: '=';
CM: ',';
DOT: '.';
LB: '(';
RB: ')';
LS: '[';
RS: ']';
LP: '{';
RP: '}';

// LITERAL
INTLIT: '0' | [1-9](('_')?[0-9])* {self.text = self.text.replace('_', '')};

FLOATLIT: (INTLIT DECPART EXPPART |INTLIT DECPART | INTLIT EXPPART | DECPART EXPPART) {self.text = self.text.replace('_', '')};
fragment DECPART: DOT [0-9]*;
fragment EXPPART: [eE] (ADDOP | SUBOP)? [0-9]+;

TRUE: 'true';
FALSE: 'false';

STRINGLIT: '"' CHAR* '"' {self.text = self.text[1:-1]};
fragment ESCAPE: '\\' [\\'bfnrt"];
fragment CHAR: ~["\\\r\n'] | ESCAPE;

// INDENTIFIER
ID: [a-zA-Z_] [a-zA-Z_0-9]*;

WS : [ \t\r\n]+ -> skip ; // skip spaces, tabs, newlines

fragment ESCAPE_ILLEGAL: '\\' ~[btnfr"\\] | '\\';
UNCLOSE_STRING_1: '"' CHAR* {raise UncloseString(self.text[1:])};
UNCLOSE_STRING_2: '"' CHAR* '\\' [bnr] {raise UncloseString(self.text[1:-1])};
ILLEGAL_ESCAPE: '"' CHAR* ESCAPE_ILLEGAL {raise IllegalEscape(self.text[1:])};
ERROR_CHAR: . {raise ErrorToken(self.text)};