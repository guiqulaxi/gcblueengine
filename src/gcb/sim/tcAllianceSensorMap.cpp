/**
**  @file tcSensorMap.cpp
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

#include "tcAllianceSensorMap.h"
#include "aerror.h"
#include "simmath.h"
#include "tcSimState.h"
#include "tcWeaponObject.h"
#include "tcPlatformDBObject.h"
#include "common/tcObjStream.h"
#include "tcGameStream.h"
#include "tcDatabaseIterator.h"
#include "tcAllianceInfo.h"
#include "tcSensorTrackIterator.h"
#include <cassert>
#ifdef _DEBUG
#define new DEBUG_NEW
#endif




/******************************* tcAllianceSensorMap ****************************/

/**
* Loads state from update stream.
*/
tcUpdateStream& tcAllianceSensorMap::operator<<(tcUpdateStream& stream)
{
    unsigned int nUpdates;
    stream >> nUpdates;

    for (unsigned int n=0; n<nUpdates; n++)
    {
        long nTrackID;
        stream >> nTrackID;

        long nIdx = maTrackToSensorTrack[nTrackID];
        if (nIdx == NULL_INDEX)
        {
            std::shared_ptr<tcSensorMapTrack>psmtrack = std::make_shared<tcSensorMapTrack>();
            long nKey;
            maTrack.AddElement(psmtrack, nKey);
            maTrackToSensorTrack[nTrackID] = nKey;
            (*psmtrack) << stream;
        }
        else 
        {
            std::shared_ptr<tcSensorMapTrack >psmtrack;
            if (maTrack.Lookup(nIdx, psmtrack) == false)
            {
                fprintf(stderr, "tcAllianceSensorMap::operator<< -- "
                                "sensor map index corrupt\n");
                return stream;
            }
            (*psmtrack) << stream;
        }

    }

    return stream;
}

/**
* Saves state to update stream
* Iterates through tracks, saving tracks that have been recently
* updated to stream.
*/
tcUpdateStream& tcAllianceSensorMap::operator>>(tcUpdateStream& stream)
{
    long freeSpace = stream.GetMaxSize() - stream.size() - sizeof(unsigned int); // unsigned int for update count header

    // if freeSpace < 0, the message should be rejected anyway so don't worry about special case
    // for this

    tcUpdateStream tempStream1;
    tcUpdateStream tempStream2;
    unsigned int nUpdates = 0;

    long pos;
    if (nextUpdateKey == -1)
    {
        pos = maTrack.GetStartPosition();
        updatesRemaining = maTrack.GetCount();
    }
    else
    {
        pos = nextUpdateKey;
    }


    std::shared_ptr<tcSensorMapTrack> sensorMapTrack ;
 
    while ((updatesRemaining > 0) && (freeSpace > 0))
    {
        tempStream1.clear();
        
        maTrack.GetNextAssoc(pos, nextUpdateKey, sensorMapTrack);
        updatesRemaining--;
        double dt = mfPreviousStatusTime - sensorMapTrack->mfTimestamp;
        if (dt < 2.0)
        {
            tempStream1 << sensorMapTrack->mnID;
            *sensorMapTrack >> tempStream1;

            if ((long)tempStream1.size() <= freeSpace)
            {
                tempStream2 << tempStream1;
                freeSpace -= tempStream1.size();
                nUpdates++;
            }
            else
            {
                freeSpace = 0;
                updatesRemaining++; // have to redo this update
            }

        }

    }

    if (nUpdates == 0)
    {
        nextUpdateKey = -1;
        updatesRemaining = 0;
        stream.SetDoneFlag(true);
        return stream;
    }

    stream << nUpdates;
    stream << tempStream2;

    if (updatesRemaining < 0)
    {
        assert(updatesRemaining == 0);
        nextUpdateKey = -1;
        updatesRemaining = 0;
        stream.SetDoneFlag(true);
    }
    else
    {
        stream.SetDoneFlag(false);
    }



    return stream;
}


/**
* Save
*/
tcGameStream& tcAllianceSensorMap::operator>>(tcGameStream& stream)
{    
    // save track to sensor track lookup
    for (int k=0; k<MAX_TRACKS; k++)
    {
	    stream << maTrackToSensorTrack[k];
    }

    // save track count
    tcSensorTrackIterator iterCount(alliance);
    unsigned int nTracks = 0;
    for (iterCount.First(); iterCount.NotDone(); iterCount.Next())
    {
        nTracks++;
    }
    stream << nTracks;

    // save track data
    tcSensorTrackIterator iter(alliance);
    for (iter.First(); iter.NotDone(); iter.Next())
    {
        std::shared_ptr<tcSensorMapTrack> track = iter.Get();
        *track >> stream;
    }

    // save other member variables
	stream << mfPreviousStatusTime;
	stream << lastEngagementsUpdate;
    stream << nextUpdateKey;
    stream << updatesRemaining;

    return stream;
}

/**
* Load
*/
tcGameStream& tcAllianceSensorMap::operator<<(tcGameStream& stream)
{
    Clear();

    // load track to sensor track lookup
    for (int k=0; k<MAX_TRACKS; k++)
    {
	    stream >> maTrackToSensorTrack[k];
    }

    // load track count
    unsigned int nTracks;
    stream >> nTracks;

    // load tracks
    for (unsigned int k=0; k<nTracks; k++)
    {
        // std::shared_ptr<tcSensorMapTrack> track = new tcSensorMapTrack;
        std::shared_ptr<tcSensorMapTrack>track = std::make_shared<tcSensorMapTrack>();

        *track << stream;

        long mapId = maTrackToSensorTrack[track->mnID];
        maTrack.AddElementForceKey(track, mapId);
    }

    // load other member variables
	stream >> mfPreviousStatusTime;
	stream >> lastEngagementsUpdate;
    stream >> nextUpdateKey;
    stream >> updatesRemaining;

    return stream;
}

void tcAllianceSensorMap::AddAlwaysVisibleTrack(std::shared_ptr<tcGameObject> obj)
{
    assert(obj != 0);
    if (obj == 0) return;

    std::shared_ptr<tcSensorMapTrack>track =nullptr;
    long nTrackID = obj->mnID;
    long nIdx = maTrackToSensorTrack[nTrackID];
    if (nIdx == NULL_INDEX)
    {
        track = std::make_shared<tcSensorMapTrack>();
        long nKey;
        maTrack.AddElement(track, nKey);
        maTrackToSensorTrack[nTrackID] = nKey;
    }
    else // already exists
    {
        if (maTrack.Lookup(nIdx, track) == false)
        {
            fprintf(stderr, "tcAllianceSensorMap::AddAlwaysVisibleTrack - sensor map index corrupt\n");
            assert(false);
            return;
        }
    }


    assert(track != 0);

    track->alwaysVisible = true;
    track->mnID = obj->mnID;
    track->mfLat_rad = obj->mcKin.mfLat_rad;
    track->mfLon_rad = obj->mcKin.mfLon_rad;
    track->mfAlt_m = obj->mcKin.mfAlt_m;
    track->mfTimestamp = obj->mfStatusTime;
    track->mnFlags = TRACK_ACTIVE | TRACK_ALT_VALID | TRACK_SPEED_VALID;
    track->mfHeading_rad = 0;
    track->mfSpeed_kts = 0;

    UINT16 nClassification = obj->mpDBObject->mnType;
    tcAllianceInfo::Affiliation affil = tcAllianceInfo::Get()->GetAffiliation(GetAlliance(), obj->GetAlliance());

    track->UpdateClassification(nClassification);
    track->IdentifyTrack(obj->mpDBObject->mnKey);
    track->SetAffiliation(affil);

    tcSensorReport report;
    report.timeStamp = obj->mfStatusTime;
    track->AddReport(report);
}

/**
* Used to "cheat" and immediately mark track corresponding to tcGameObject as destroyed
*/
void tcAllianceSensorMap::MarkObjectDestroyed(std::shared_ptr<const tcGameObject> obj)
{
	assert(obj != 0);
    if (obj == 0) return;

    std::shared_ptr<tcSensorMapTrack>track =nullptr;

    long objectID = obj->mnID;
    long nIdx = maTrackToSensorTrack[objectID];
    if (nIdx != NULL_INDEX)
    {
		maTrack.Lookup(nIdx, track);
    }
	else
	{
		return; // don't have this
	}

	assert(track != 0);
	track->MarkDestroyed();
}



tcSensorReport* tcAllianceSensorMap::GetOrCreateReport(long platformID, long sensorID, long trackID, std::shared_ptr<tcSensorMapTrack>& pSMTrack)
{
    pSMTrack = 0;
    long nIdx = maTrackToSensorTrack[trackID];
    if (nIdx == NULL_INDEX) 
    {
        std::shared_ptr<tcSensorMapTrack>psmtrack = std::make_shared<tcSensorMapTrack>();
        long nKey;
        maTrack.AddElement(psmtrack, nKey);
        maTrackToSensorTrack[trackID] = nKey;
        psmtrack->mnID = trackID;

        pSMTrack = psmtrack;

        return psmtrack->GetOrCreateReport(platformID, sensorID);
    }
    else
    {
        std::shared_ptr<tcSensorMapTrack>psmtrack;

        if (maTrack.Lookup(nIdx, psmtrack) == true) 
        {
            pSMTrack = psmtrack;
            return psmtrack->GetOrCreateReport(platformID, sensorID);
        }
        else
        {
            fprintf(stderr, "Error - sensor map index corrupt");
            assert(false);
            return 0;
        }
    }
}


void tcAllianceSensorMap::ValidateMap()
{
#ifdef _DEBUG
    long cmappos = maTrack.GetStartPosition();
    long nSize = maTrack.GetCount();
    long nKey;
    std::shared_ptr<tcSensorMapTrack> psmtrack;

    for (long i=0;i<nSize;i++) 
    {
        maTrack.GetNextAssoc(cmappos,nKey,psmtrack);

       
        assert(psmtrack != 0);
        assert(psmtrack->mnID >= 0);
        assert(psmtrack->mnID < 512);

        assert(psmtrack->GetContributorCount() <= tcSensorMapTrack::MAX_SENSOR_REPORTS);
        assert(nKey >= 0);

        long poolKey = maTrackToSensorTrack[psmtrack->mnID];
        assert(poolKey == nKey);

        unsigned int nContributors = psmtrack->GetContributorCount();
        for (unsigned int n=0; n<nContributors; n++)
        {
            assert(psmtrack->maSensorReport[n].startTime <= psmtrack->maSensorReport[n].timeStamp);
        }
    }


    assert(maTrack.CheckForCorruption() == false);

    for (size_t n=0; n<MAX_TRACKS; n++)
    {
        long idx = maTrackToSensorTrack[n];
        if (idx != NULL_INDEX) 
        {
            std::shared_ptr<tcSensorMapTrack> psmtrack;
            if (maTrack.Lookup(idx, psmtrack) == false) 
            {
                assert(false);
            }
        }
    }
#endif
}


int tcAllianceSensorMap::GetTrackCount() 
{
    return maTrack.GetCount();
}

long tcAllianceSensorMap::GetStartTrackPosition() 
{
    return maTrack.GetStartPosition();
}

void tcAllianceSensorMap::GetNextTrack(long& pos, std::shared_ptr<tcSensorMapTrack>& pTrack)
{
    long nKey;
    maTrack.GetNextAssoc(pos, nKey, pTrack);
}

#define SENSORMAP_AGEOUTTIME 30.0f

void tcAllianceSensorMap::DropTrack(long anID)
{
    std::shared_ptr<tcSensorMapTrack> track = GetSensorMapTrack(anID);
	if (track == 0)
	{
		fprintf(stderr, "Error - tcAllianceSensorMap::DropTrack - track does not exist\n");
		return;
	}

	track->Clear();

    long nKey = maTrackToSensorTrack[anID];
    if (nKey == NULL_INDEX) 
	{
		fprintf(stderr, "Error - tcAllianceSensorMap::DropTrack - track does not exist (B)\n");
		return;
	} 

    maTrackToSensorTrack[anID] = -1;
    maTrack.RemoveKey(nKey);
}


void tcAllianceSensorMap::UpdateMultiplayerClient(double statusTime)
{
    long cmappos = maTrack.GetStartPosition();
    long nSize = maTrack.GetCount();
    long nKey;
    std::shared_ptr<tcSensorMapTrack> psmtrack;

    for (long i=0;i<nSize;i++) 
    {
        maTrack.GetNextAssoc(cmappos,nKey,psmtrack);

        double timeSinceUpdate = statusTime - psmtrack->mfTimestamp;

        float ageOutTime = psmtrack->GetAgeOutTime();

        // updated to never drop ground tracks
        bool dropTrack = (timeSinceUpdate > ageOutTime);

        if (dropTrack)
        {
            if (psmtrack->mnID >= 0) 
            {
                maTrackToSensorTrack[psmtrack->mnID] = NULL_INDEX; // used to be = maTrack.GetPoolSize();
            }
            char zBuff[128];
            sprintf(zBuff,"Dropped track %d at time %.1f",psmtrack->mnID,statusTime);
            WTL(zBuff);

            maTrack.RemoveKey(nKey);
        }
        else 
        {
            // check for new data and update
            //psmtrack->UpdateTrack(); // never called for client
        }
    }

#ifdef _DEBUG
    assert(maTrack.CheckForCorruption()==false);
#endif
}

// 更新传感器地图状态
void tcAllianceSensorMap::Update(double statusTime)
{
    // 如果状态时间间隔小于1秒，则不执行更新
    if ((statusTime - mfPreviousStatusTime) < 1.0f) {
        return;
    }
    // 更新上一次状态时间
    mfPreviousStatusTime = statusTime;

    // 如果是多人游戏的客户端，则更新客户端特定的逻辑
    if (tcSimState::Get()->IsMultiplayerClient())
    {
        UpdateMultiplayerClient(statusTime);
        return;
    }

    // 获取追踪列表的起始位置和大小
    long cmappos = maTrack.GetStartPosition();
    long nSize = maTrack.GetCount();
    long nKey;
    std::shared_ptr<tcSensorMapTrack> psmtrack;

    // 检查是否需要更新交战信息
    bool updateEngagements = false;
    if (statusTime - lastEngagementsUpdate > 8.0f)
    {
        updateEngagements = true;
        lastEngagementsUpdate = statusTime;
    }

    // 遍历所有追踪项
    for (long i=0; i<nSize; i++)
    {
        maTrack.GetNextAssoc(cmappos,nKey,psmtrack);

        // 标记是否有非陈旧报告
        bool freshReport = false;

        // 用于存储需要移除的报告索引
        std::vector<size_t> reportsToRemove;

        // 获取追踪的陈旧时间和过期时间
        float staleTime = psmtrack->GetStaleTime();
        float ageOutTime = psmtrack->GetAgeOutTime();

        // 遍历所有贡献者（可能是传感器报告）
        size_t nContributors = psmtrack->GetContributorCount();
        for (size_t n=0; n<nContributors; n++)
        {
            // 计算自上次更新以来的时间
            double timeSinceUpdate = statusTime - psmtrack->maSensorReport[n].timeStamp;
            // 如果报告已过期，则添加到移除列表
            if (timeSinceUpdate >= ageOutTime)
            {
                reportsToRemove.push_back(n);
            }
            // 如果报告陈旧但未过期，且目标已销毁且时间足够长，也添加到移除列表
            else if (timeSinceUpdate >= staleTime)
            {
                if (psmtrack->IsDestroyed() && (timeSinceUpdate >= staleTime + 10.0))
                {
                    reportsToRemove.push_back(n);
                }
            }
            // 否则，标记为有新鲜报告
            else
            {
                freshReport = true;
            }
        }

        // 移除需要移除的报告
        if (reportsToRemove.size() > 0)
        {
            psmtrack->RemoveReports(reportsToRemove);
        }

        // 如果没有新鲜报告，则定期更新追踪以使其保持活动状态（可能用于多人游戏客户端）
        if (!freshReport)
        {
            if (statusTime - psmtrack->mfTimestamp > 10.0f)
            {
                psmtrack->UpdateTrack(statusTime);
            }
            psmtrack->MarkStale(); // 注意：UpdateTrack中可能会清除陈旧状态
        }

        // 检查是否应删除追踪项（无贡献者且非始终可见）
        bool dropTrack = (psmtrack->GetContributorCount() == 0) && (!psmtrack->alwaysVisible);

        // 如果需要删除追踪项
        if (dropTrack)
        {
            // 清理与追踪ID相关的映射（如果存在）
            if (psmtrack->mnID >= 0)
            {
                maTrackToSensorTrack[psmtrack->mnID] = NULL_INDEX; // 注意：这里之前可能是设置为maTrack.GetPoolSize()，但现在是NULL_INDEX
            }

            // 从追踪列表中移除该追踪项
            maTrack.RemoveKey(nKey);

            // 调试信息
#ifdef _DEBUG
            char zBuff[128];
            sprintf(zBuff,"Dropped track %d at time %.1f",psmtrack->mnID,statusTime);
            WTL(zBuff); // 假设WTL是某种日志或跟踪函数
#endif

        }
        else
        {
            // 如果有新数据或需要更新，则更新追踪项
            psmtrack->UpdateTrack(0);
            // 如果需要更新交战信息
            if (updateEngagements)
            {
                psmtrack->UpdateEngagements();
                psmtrack->UpdateIntercepts();
            }
        }
    }

    // 调试断言，检查追踪列表是否损坏
#ifdef _DEBUG
    assert(maTrack.CheckForCorruption()==false);
#endif
}
unsigned int tcAllianceSensorMap::GetAlliance() const
{
	return alliance;
}

/*******************************************************************************/
std::shared_ptr<tcSensorMapTrack> tcAllianceSensorMap::GetSensorMapTrack(long anTrackID)
{
    long nMapID;
    std::shared_ptr<tcSensorMapTrack> psmtrack;

    if (anTrackID >= MAX_TRACKS) {return NULL;}
    nMapID = maTrackToSensorTrack[anTrackID];
    if (nMapID == NULL_INDEX) {return NULL;}
    maTrack.Lookup(nMapID,psmtrack);
    return psmtrack;
}

std::vector<tcSensorReport > tcAllianceSensorMap::GetSensorReport(long platformID)
{
    std::vector<tcSensorReport> result;
    long cmappos = maTrack.GetStartPosition();
    long nKey;
     std::shared_ptr<tcSensorMapTrack>  track;
    for (size_t i = 0; i < maTrack.GetCount(); ++i) {
         maTrack.GetNextAssoc(cmappos,nKey,track);
        if ( track->IsValid()) {
            for (const auto& report : track->maSensorReport) {
                if ( report.platformID == platformID) {
                    result.push_back(report);
                }
            }
        }
    }

    return result;
}
/*******************************************************************************/
bool tcAllianceSensorMap::GetTrack(long anTrackID, tcTrack& track) 
{
    std::shared_ptr<tcSensorMapTrack> pSensorTrack = GetSensorMapTrack(anTrackID);

    if (pSensorTrack == nullptr)
	{
        return false;
    }
    track = *(pSensorTrack);
    return true;
}

/*******************************************************************************/
void tcAllianceSensorMap::Clear() 
{
    maTrack.RemoveAll();
    for(long k=0;k<MAX_TRACKS;k++) 
    {
        maTrackToSensorTrack[k] = NULL_INDEX;
    }
    // randomize updates so alliances don't all update at once
    mfPreviousStatusTime = 1.0f*randf();
    lastEngagementsUpdate = 10.0f*randf();

    nextUpdateKey = -1;
    updatesRemaining = 0;
}
/********************************************************************/
int tcAllianceSensorMap::Serialize(tcFile& file, bool mbLoad) {
    long nMapSize, nKey;
    std::shared_ptr<tcSensorMapTrack> psmtrack;

    /* load SensorMap from file */
    if (mbLoad) {
        Clear();

        file.Read(maTrackToSensorTrack,MAX_TRACKS*sizeof(long));
        file.Read(&nMapSize,sizeof(nMapSize));
        for(int i=0;i<nMapSize;i++) {
            psmtrack = std::make_shared<tcSensorMapTrack>();
            file.Read(psmtrack.get(),sizeof(tcSensorMapTrack));
            if ((unsigned long)psmtrack->mnID >= MAX_TRACKS) {
                WTL("tcAllianceSensorMap::Serialize - corrupt scenario file");
                return false;
            }
            nKey = maTrackToSensorTrack[psmtrack->mnID];
            maTrack.AddElementForceKey(psmtrack,nKey);
        }
    }
    /* save to file */
    else {   
        long cmappos = maTrack.GetStartPosition();

        file.Write(maTrackToSensorTrack,MAX_TRACKS*sizeof(long));

        nMapSize = maTrack.GetCount();
        file.Write(&nMapSize,sizeof(nMapSize));
        for (long i=0;i<nMapSize;i++) {
            maTrack.GetNextAssoc(cmappos,nKey,psmtrack);
            file.Write(psmtrack.get(),sizeof(tcSensorMapTrack));
        }  
    }
    return true;
}

tcAllianceSensorMap::tcAllianceSensorMap(unsigned int mapAlliance) 
: alliance(mapAlliance),
  nextUpdateKey(-1),
  updatesRemaining(0)
{
    Clear();

    bool autoKillAssessment = tcOptions::Get()->OptionStringExists("AutoKillAssessment");
    tcSensorMapTrack::SetAutoKillAssess(autoKillAssessment);
    
}

tcAllianceSensorMap::~tcAllianceSensorMap() 
{
}
