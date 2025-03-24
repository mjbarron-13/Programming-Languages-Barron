%{
    #include "parser.tab.h"
    #include <string.h>
%}

%%

[0-9]+      { yylval.num = atoi(yytext); return NUMBER; }
[+\-*/()]   { return yytext[0]; }
"\n"        { return '\n'; }   // This ensures single expressions are processed
[ \t]       { /* Ignore whitespace */ }
exit        { printf("Exiting...\n"); exit(0); }
.           { printf("Unrecognized character: %s\n", yytext); }

%%

int yywrap() { return 1; }
