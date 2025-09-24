grammar Modificado;
options { caseInsensitive=true; }

prog:	stat+ ;

stat:	expr NEWLINE         	#printExpr
    |	'modo=' ID NEWLINE 	#Modo
    |	NEWLINE			#blank
    ;

expr:	term op=('*'|'/') expr		#MulDiv
    |	term				#Toterm
    ;
    
term:	fact op=('+'|'-') term			#AddSub
    |	fact					#Tofactor
    ;
    
fact:	'Sqrt(' expr ')'			#Raiz
    |	op=('ln'|'log') '(' expr ')'		#Log
    |	op=('sin'|'cos'|'tan') '(' expr ')'  	#SinCosTan
    |	fact '!'				#Factor
    |	INT					#int
    |	ID					#id
    |	'(' expr ')'				#parens
    ;
    
MUL: '*' ;
DIV: '/' ;
ADD: '+' ;
SUB: '-' ;

ID: [a-z]+ ;      
INT: [0-9]+ ;                    
NEWLINE: [\r\n]+ ;             
WS: [ \t]+ -> skip ;
