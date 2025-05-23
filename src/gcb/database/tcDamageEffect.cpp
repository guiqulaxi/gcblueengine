/**  
**  @file tcDamageEffect.cpp
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


#if _MSC_VER > 1000
#pragma warning(disable:4786) // suppress warning for STL bug in VC6, see Q167355 in the MSDN Library.
#endif // _MSC_VER > 1000


#include "tcDamageEffect.h"
#include <cassert>
#include "strutil.h"
#ifdef _DEBUG
#define new DEBUG_NEW
#endif

using namespace std;

namespace database
{


/**
* @return damage factor based on linear interpolation
*/
float tcDamageEffect::GetDamageFactor(const std::vector<DamagePoint>& damageTable, float level) const
{
    if (level <= 0) return 0;

    size_t nTable = damageTable.size();

    if (nTable == 0)
    {
        assert(false);
        return 0;
    }

    if (level <= damageTable[0].effectLevel) return damageTable[0].damageFactor;
    if (level >= damageTable[nTable-1].effectLevel) return damageTable[nTable-1].damageFactor;

    assert(nTable > 1);
    for (size_t n=0; n<nTable-1; n++)
    {
        float step = damageTable[n+1].effectLevel - damageTable[n].effectLevel;

        if ((level > damageTable[n].effectLevel) && (level <= damageTable[n+1].effectLevel))
        {
            if (step > 0)
            {
                float alpha = (damageTable[n+1].effectLevel - level) / step;
                return alpha * damageTable[n].damageFactor + (1.0 - alpha) * damageTable[n+1].damageFactor;
            }
            else
            {
                return damageTable[n].damageFactor;
            }
        }
    }

    assert(false);
    return 0;
}


float tcDamageEffect::GetBlastDamageFactor(float level) const
{
    return GetDamageFactor(blastEffect, level);
}

float tcDamageEffect::GetFragmentDamageFactor(float level) const
{
    return GetDamageFactor(fragEffect, level);
}

float tcDamageEffect::GetRadiationDamageFactor(float level) const
{
    return GetDamageFactor(radEffect, level);
}

float tcDamageEffect::GetInternalDamageFactor(float level) const
{
    return GetDamageFactor(internalEffect, level);
}

float tcDamageEffect::GetWaterBlastDamageFactor(float level) const
{
    return GetDamageFactor(waterBlastEffect, level);
}

/**
* @return false if error in parse, otherwise true
*/
bool tcDamageEffect::ParseEffectString(std::vector<DamagePoint>& effect, const std::string& effectString)
{
    effect.clear();

    std::string s(effectString);

    unsigned int nIterations = 0;
    const unsigned int maxIterations = 48;
    auto splits=strutil::split(s,';');
    for(int nIterations=0;nIterations<maxIterations&&nIterations<splits.size();nIterations++)
    {
       strutil::trim(splits[nIterations]);
       double effectLevel = 0;
       double damageFactor = 0;
       try {
           effectLevel=std::stod(strutil::split(splits[nIterations],' ')[0]);
           damageFactor=std::stod(strutil::split(splits[nIterations],' ')[1]);
       } catch (...) {

       }

       DamagePoint point;
       point.effectLevel = (float)effectLevel;
       //point.damageFactor = 2.0f * (float)damageFactor; // double here to make factor in database the MEDIAN damage with uniform rand
       point.damageFactor = (float)damageFactor;
       // Amram - calming this down, a fluctuation from 0 through 200% is a bit much?  Replacing the other piece of the random factor
       //		   to achieve 100%  30%, for a range from 70% through 130%.

       effect.push_back(point);
    }
//    while ((s.size() > 2) && (++nIterations < maxIterations))
//    {
//        wxString s1 = s.BeforeFirst(';');
//        s1.Trim(false); // remove whitespace from left

//        double effectLevel = 0;
//        double damageFactor = 0;
//        if (s1.BeforeFirst(' ').ToDouble(&effectLevel) == false)
//        {
//            return false;
//        }

//        if (s1.AfterFirst(' ').ToDouble(&damageFactor) == false)
//        {
//            return false;
//        }

//        DamagePoint point;
//        point.effectLevel = (float)effectLevel;
//        //point.damageFactor = 2.0f * (float)damageFactor; // double here to make factor in database the MEDIAN damage with uniform rand
//        point.damageFactor = (float)damageFactor;
//		// Amram - calming this down, a fluctuation from 0 through 200% is a bit much?  Replacing the other piece of the random factor
//		//		   to achieve 100%  30%, for a range from 70% through 130%.

//        effect.push_back(point);

//        s = s.AfterFirst(';');
//    }

    return (nIterations < maxIterations);
    
}


tcDamageEffect::tcDamageEffect()
{

}

tcDamageEffect::tcDamageEffect(const tcDamageEffect& obj)
: tcTableObject(obj),
  blastEffect(obj.blastEffect),
  fragEffect(obj.fragEffect),
  radEffect(obj.radEffect),
  internalEffect(obj.internalEffect)
{
}

tcDamageEffect::tcDamageEffect(const std::string& s)
: tcTableObject(s)
{
}

tcDamageEffect::tcDamageEffect(sqlite3x::sqlite3_reader& reader)
: tcTableObject(reader)
{
    std::string effectString = reader.getstring(1);
    ParseEffectString(blastEffect, effectString);

    effectString = reader.getstring(2);
    ParseEffectString(waterBlastEffect, effectString);

    effectString = reader.getstring(3);
    ParseEffectString(fragEffect, effectString);

    effectString = reader.getstring(4);
    ParseEffectString(radEffect, effectString);

    effectString = reader.getstring(5);
    ParseEffectString(internalEffect, effectString);

}

void tcDamageEffect::WritePythonValue( std::string &valueString) const
{
    tcTableObject::WritePythonValue(valueString);
    valueString+="    dbObj.blastEffect=[pygcb.DamagePoint()]*"+std::to_string(blastEffect.size())+"\n";
    for (size_t i=0 ; i < blastEffect.size(); ++i) {
        valueString+="    dbObj.blastEffect["+std::to_string(i)+"].effectLevel="+strutil::to_python_value(blastEffect[i].effectLevel)+"\n";
        valueString+="    dbObj.blastEffect["+std::to_string(i)+"].damageFactor="+strutil::to_python_value(blastEffect[i].damageFactor)+"\n";
    }
    valueString+="    dbObj.waterBlastEffect=[pygcb.DamagePoint()]*"+std::to_string(waterBlastEffect.size())+"\n";
    for (size_t i=0 ; i < waterBlastEffect.size(); ++i) {
        valueString+="    dbObj.waterBlastEffect["+std::to_string(i)+"].effectLevel="+strutil::to_python_value(waterBlastEffect[i].effectLevel)+"\n";
        valueString+="    dbObj.waterBlastEffect["+std::to_string(i)+"].damageFactor="+strutil::to_python_value(waterBlastEffect[i].damageFactor)+"\n";
    }
    valueString+="    dbObj.fragEffect=[pygcb.DamagePoint()]*"+std::to_string(fragEffect.size())+"\n";
    for (size_t i=0 ; i < fragEffect.size(); ++i) {
        valueString+="    dbObj.fragEffect["+std::to_string(i)+"].effectLevel="+strutil::to_python_value(fragEffect[i].effectLevel)+"\n";
        valueString+="    dbObj.fragEffect["+std::to_string(i)+"].damageFactor="+strutil::to_python_value(fragEffect[i].damageFactor)+"\n";
    }
    valueString+="    dbObj.radEffect=[pygcb.DamagePoint()]*"+std::to_string(radEffect.size())+"\n";
    for (size_t i=0 ; i < radEffect.size(); ++i) {
        valueString+="    dbObj.radEffect["+std::to_string(i)+"].effectLevel="+strutil::to_python_value(radEffect[i].effectLevel)+"\n";
        valueString+="    dbObj.radEffect["+std::to_string(i)+"].damageFactor="+strutil::to_python_value(radEffect[i].damageFactor)+"\n";
    }
    valueString+="    dbObj.internalEffect=[pygcb.DamagePoint()]*"+std::to_string(internalEffect.size())+"\n";
    for (size_t i=0 ; i < internalEffect.size(); ++i) {
        valueString+="    dbObj.internalEffect["+std::to_string(i)+"].effectLevel="+strutil::to_python_value(internalEffect[i].effectLevel)+"\n";
        valueString+="    dbObj.internalEffect["+std::to_string(i)+"].damageFactor="+strutil::to_python_value(internalEffect[i].damageFactor)+"\n";
    }


}

void tcDamageEffect::WritePython( std::string &valueString) const
{
    valueString+="import pygcb\n";
    valueString+="def CreateDBObject():\n";
    valueString+="    dbObj=pygcb.tcDamageEffect()\n";
    WritePythonValue(valueString);
    valueString+="    return dbObj\n";
}

tcDamageEffect::~tcDamageEffect() 
{
}


}
