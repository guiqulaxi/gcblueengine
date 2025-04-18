/**
**  @file tcECM.h
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

#ifndef _tcECM_H_
#define _tcECM_H_

#if _MSC_VER > 1000
#pragma once
#endif

#include "tcSensorState.h"
#include "tcDatabase.h"
#include "tcECMDBObject.h"
#include <vector>

class tcGameObject;
class tcRadar;
class tcStream;
class tcGameStream;

using namespace database;

/**
* For safe access of std::shared_ptr<tcRadar> pointer
*/
class RadarInterface
{
public:
    long id; ///< platform id
    unsigned idx; ///< sensor index

    std::shared_ptr<tcRadar> GetRadar(); ///< returns 0 if platform or sensor doesn't exist anymore

    tcGameStream& operator<<(tcGameStream& stream);
    tcGameStream& operator>>(tcGameStream& stream);

    RadarInterface(long id_, unsigned idx_);
    RadarInterface(const RadarInterface& src);
    RadarInterface();
    
    ~RadarInterface();
};

/**
 *电子对抗措施（ECM）包含了进攻性的有源电子干扰和防御性的有源无源诱饵等自卫干扰手段。电子支援系统截获并分析出的敌方辐射源类型、频率、方位等信息后，电子干扰就可以大举“进攻”。
 */
class tcECM : public tcSensorState
{
    friend class tcECMEvaluationDialog;
public:
    std::shared_ptr<tcECMDBObject> mpDBObj;

    virtual bool InitFromDatabase(long key); ///< initializes sensor using database data at key

	virtual bool IsECM() const;

    void Serialize(tcFile& file, bool mbLoad);
    virtual void SetActive(bool active);
    virtual void Update(double t);

    tcECM& operator=(tcECM& ss);
    //virtual tcStream& operator<<(tcStream& stream);
    //virtual tcStream& operator>>(tcStream& stream);

    virtual tcGameStream& operator<<(tcGameStream& stream);
    virtual tcGameStream& operator>>(tcGameStream& stream);

    std::shared_ptr<tcECM> Clone();
    tcECM();
    tcECM(std::shared_ptr<tcECMDBObject> dbObj);
    virtual ~tcECM();

private:
    std::vector<RadarInterface> jamList; ///< radars jammed on previous update
    
    void AddOrUpdateJammerToTarget(std::shared_ptr<tcRadar> targetRadar, unsigned sensorIdx, float JNR_dB,
             float jammerBearing_rad, float jammerElevation_rad);
    void ClearJamList();

    void UpdateBarrage();
    void UpdateBarrageTarget(std::shared_ptr<tcGameObject> target);
    void UpdateBarrageTargetRadar(std::shared_ptr<tcRadar> radar, unsigned sensorIdx);
};
#endif
