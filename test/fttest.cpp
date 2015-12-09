#include <stdio.h>
#include <string.h>
#include <ft2build.h>
#include FT_FREETYPE_H


FT_Library  library;

int main()
{
  FT_Error error = FT_Init_FreeType( &library );
  if ( error )
  {
    return 1;
  }

  return 0;
}
