%{
    #include <stdio.h>
    #include <stdlib.h>

    void yyerror(const char *s);
    int yylex();
%}

%union {
    int num;
}

%token <num> NUMBER
%left '+' '-'
%left '*' '/'
%type <num> expr

%%

input: /* Allows multiple expressions */
    | input expr '\n' { printf("= %d\n", $2); }
    ;

expr: expr '+' expr  { $$ = $1 + $3; }
    | expr '-' expr  { $$ = $1 - $3; }
    | expr '*' expr  { $$ = $1 * $3; }
    | expr '/' expr  { 
        if ($3 == 0) {
            yyerror("Division by zero!");
            YYABORT;
        }
        $$ = $1 / $3;
    }
    | '(' expr ')'  { $$ = $2; }
    | NUMBER        { $$ = $1; }
    ;

%%

void yyerror(const char *s) {
    printf("Error: %s\n", s);
}

int main() {
    printf("Enter arithmetic expressions (one per line, type 'exit' to quit):\n");

    while (1) {
        printf("> ");
        if (yyparse()) {
            break;
        }
    }

    printf("Calculator exited.\n");
    return 0;
}
