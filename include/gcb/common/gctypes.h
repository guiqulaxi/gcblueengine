#ifndef _GCTYPES_H_
#define _GCTYPES_H_

// could be platform dependent
// these are also defined through windows.h or afxwin.h
// and may lead to duplicate or ambiguous definition problems

#ifndef UINT8
typedef unsigned char UINT8;
#endif

#ifndef UINT16
typedef unsigned short UINT16;
#endif

#ifndef INT16
typedef short INT16;
#endif

#ifndef UINT32
typedef unsigned int UINT32;
#endif

#ifndef UINT
typedef unsigned int UINT;
#endif

#ifndef UCHAR
typedef unsigned char UCHAR;
#endif

// Only define DWORD if not already defined by system headers


//#ifndef Uint_PTR
//typedef unsigned int Uint_PTR;
//#endif

#ifndef WIN32 // to avoid visual 7 error related to redefinition

#ifndef DWORD
typedef unsigned int DWORD;
#endif

#ifndef LARGE_INTEGER
typedef long long LARGE_INTEGER;
#endif


#ifndef WCHAR
typedef unsigned int WCHAR;
#endif

#ifndef intint
typedef unsigned int intint;
#endif

#endif // WIN32

#endif // _GCTYPES_H_
