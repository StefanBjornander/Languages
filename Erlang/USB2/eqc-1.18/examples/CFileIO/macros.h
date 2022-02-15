// These macros make it easy to generate C code that writes Erlang terms
// in the file later to be read by QuickCheck.

int level=0;        // level of nesting inside list or tuple brackets
int comma_needed=0; // if true, a preceding term has been printed, and any
                    // following term should be preceded by a comma.

FILE* to_eqc;

void open_eqc()
{ to_eqc = fopen("to_eqc.txt","w"); }

void close_eqc()
{ fclose(to_eqc); }

void pre()
{ if(comma_needed) fprintf(to_eqc,","); }

void post()
{ if(level==0)
    { fprintf(to_eqc,".\n"); comma_needed=0; } 
  else comma_needed=1; 
}

void start_list(char *s)
{ fprintf(to_eqc,s);
  level++;
  comma_needed=0;
}

void end_list(char *s)
{ fprintf(to_eqc,s);
  level--;
  comma_needed=1;
}

// Terms are printed using these macros. Each top-level term is followed
// by a full stop and a newline, so that an entire list of terms can be
// read into Erlang by file:consult/1. List and tuple brackets, and the
// commas that separate elements, are generated automatically.

#define TERM(X) { pre();X;post(); }

// INT(n) prints an Erlang integer term with value n.

#define INT(X) TERM(fprintf(to_eqc,"%d",X))

// ATOM(s) prints an Erlang atom with name s, which should be a null-
// terminated string representing a valid Erlang atom name.

#define ATOM(S) TERM(fprintf(to_eqc,S))

// LIST(X) prints an Erlang list, where X is code to print the list 
// elements. For example, LIST(INT(1);INT(2);INT(3)) would print the 
// list [1,2,3].

#define LIST(X) TERM(start_list("[");X;end_list("]"))

// TUPLE(X) is like LIST(X), but prints a an Erlang tuple containing
// the elements printed by X, rather than a list.

#define TUPLE(X) TERM(start_list("{");X;end_list("}"))
