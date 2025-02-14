/**  
**  @file tcWeaponDamage.cpp
*/
/*
**  Copyright (c) 2014, GCBLUE PROJECT
**  All rights reserved.
**
**  Redistribution and use in source and binary forms, with or without modification, are permitted provided that the following conditions are met:
**
**  1. Redistributions of source code must retain the above copyright notice, this list of conditions and the following disclaimer.
**
**  2. Redistributions in binary form must reproduce the above copyright notice, this list of conditions and the following disclaimer in the 
**     documentation and/or other materials provided with the distribution.
**
**  3. Neither the name of the copyright holder nor the names of its contributors may be used to endorse or promote products derived from 
**     this software without specific prior written permission.
**
**  THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS" AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT 
**  NOT LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE 
**  COPYRIGHT HOLDER OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES 
**  (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) 
**  HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING 
**  IN ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.
*/

//#include "stdwx.h"

#include "strutil.h"
#if _MSC_VER > 1000
#pragma warning(disable:4786) // suppress warning for STL bug in VC6, see Q167355 in the MSDN Library.
#endif // _MSC_VER > 1000


#include "tcWeaponDamage.h"


#ifdef _DEBUG
#define new DEBUG_NEW
#endif

using namespace std;

namespace database
{



void tcWeaponDamage::WritePythonValue(std::string &valueString) const
{
    tcTableObject::WritePythonValue(valueString);
    valueString+="    dbObj.maxRange_m="+strutil::to_python_value(maxRange_m)+"\n";
    valueString+="    dbObj.probDetonate="+strutil::to_python_value(probDetonate)+"\n";
    valueString+="    dbObj.blastCharge_kg="+strutil::to_python_value(blastCharge_kg)+"\n";
    valueString+="    dbObj.fragCharge_kg="+strutil::to_python_value(fragCharge_kg)+"\n";
    valueString+="    dbObj.radCharge_kg="+strutil::to_python_value(radCharge_kg)+"\n";
    valueString+="    dbObj.fragMetal_kg="+strutil::to_python_value(fragMetal_kg)+"\n";
    valueString+="    dbObj.fragFragment_kg="+strutil::to_python_value(fragFragment_kg)+"\n";
    valueString+="    dbObj.fragSpread="+strutil::to_python_value(fragSpread)+"\n";

}

void tcWeaponDamage::WritePython(std::string &valueString) const
{
    valueString+="import pygcb\n";
    valueString+="def CreateDBObject():\n";
    valueString+="    dbObj=pygcb.tcWeaponDamage()\n";
    WritePythonValue(valueString);
    valueString+="    return dbObj\n";;
}

tcWeaponDamage::tcWeaponDamage()
: maxRange_m(0),
  probDetonate(0),
  isPenetration(false),
  blastCharge_kg(0),
  fragCharge_kg(0),
  radCharge_kg(0),
  fragMetal_kg(0),
  fragFragment_kg(1.0f),
  fragSpread(1.0f)
{

}

tcWeaponDamage::tcWeaponDamage(const tcWeaponDamage& obj) 
: tcTableObject(obj),
  maxRange_m(obj.maxRange_m),
  probDetonate(obj.probDetonate),
  isPenetration(obj.isPenetration),
  blastCharge_kg(obj.blastCharge_kg),
  fragCharge_kg(obj.fragCharge_kg),
  radCharge_kg(obj.radCharge_kg),
  fragMetal_kg(obj.fragMetal_kg),
  fragFragment_kg(obj.fragFragment_kg),
  fragSpread(obj.fragSpread)
{
}


tcWeaponDamage::tcWeaponDamage(const std::string& s)
: tcTableObject(s)
{
}

tcWeaponDamage::tcWeaponDamage(sqlite3x::sqlite3_reader& reader)
: tcTableObject(reader)
{
    maxRange_m = reader.getdouble(1);
    probDetonate = reader.getdouble(2);
    isPenetration = reader.getint(3) != 0;
    blastCharge_kg = reader.getdouble(4);
    fragCharge_kg = reader.getdouble(5);
    radCharge_kg = reader.getdouble(6);
    fragMetal_kg = reader.getdouble(7);
    fragFragment_kg = reader.getdouble(8);
    fragSpread = reader.getdouble(9);
}




tcWeaponDamage::~tcWeaponDamage() 
{
}


}
