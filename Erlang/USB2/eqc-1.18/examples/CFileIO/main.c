// This is the skeleton main program used for each test. The code generated
// by QuickCheck is included from generated.c. This main program just declares
// and initializes a few variables that the generated code needs, and opens
// and closes the file carrying results back to QuickCheck.

#include <stdio.h>
#include "macros.h"

main()
{ char buffer[1000];
  FILE* stream = fopen("data.txt","w+b");
  int i, n;
  open_eqc();
#include "generated.c"
  close_eqc();
  fclose(stream);
}
