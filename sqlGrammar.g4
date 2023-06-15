grammar sqlGrammar;

options { caseInsensitive = true; }

start: ('CREATE' | 'DATABASE' | 'INTO' | 'USE' | 'TABLE' | 'INSERT' | 'SELECT' | 'FROM' | 'ORDER' | 'BY' | 'WHERE' | 'UPDATE'
| 'SET' | 'DELETE' | 'TRUNCATE' | '(' | ')' | '<=' | '>=' | '=' | '>' | '<' | ',' | '*' | ';' | TYPE | VALUE | ID)*;

TYPE: 'int' | 'string' | 'double' | 'boolean' | 'date' | 'date_time';

VALUE: NUM | STRING;

ID: [a-z]+;

STRING: '"'ID'"' | '"''"';

NUM: INT | INT'.'INT;

INT: [0-9]+;

FLOAT: INT'.'INT;

WS: [ \t\n\r] -> skip;