/**
**  @file tcMissileDBObject.h
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

#ifndef _MISSILEDBOBJECT_H_
#define _MISSILEDBOBJECT_H_

#if _MSC_VER > 1000
#pragma once
#endif // _MSC_VER > 1000

#include "tcWeaponDBObject.h"
#include "tcAirDetectionDBObject.h"
#include <vector>



namespace database
{
   class tcSqlReader;

   /**
   * This isn't used currently. Notionally there will be different
   * damage types that have varying effectiveness vs. different
   * target types.
   */
   enum teDamageType 
   {
      DT_GENERIC
   };

   /**
   * teAltitudeMode determines how altitude is controlled for flight segment.
   */
   enum teAltitudeMode 
   {
	   /// sea level reference
	   AM_ASL = 0, 
	   /// terrain reference (altimeter)
	   AM_AGL = 1,  
	   /// set altitude to intercept if seeker has track, otherwise maintain altitude
	   AM_INTERCEPT = 2,
	   /// set altitude to impact datum
	   AM_DATUM = 3,
	   /// Intercept if higher, otherwise maintain altitude
	   AM_INTERCEPT_HIGH = 4,
	   /// Same as AM_ASL but limit max pitch
	   AM_ASL_LOFT = 5
   };

   /**
   * teGuidanceMode determines guidance type that is used flight segment.
   */
   enum teGuidanceMode 
   {
       GM_COMMAND = 0,  ///< command guidance
       GM_NAV = 1,  ///< inertial, GPS
       GM_SENSOR1 = 2, ///< use seeker
       GM_DEPLOY = 3 ///< deploy payload at start of this segment
   };

   /**
   * Info that controls missile behavior for flight segment.
   */
   struct tsMissileFlightSegment 
   {
      float mfRange_km;    ///< min range for this segment
      float mfAltitude_m;  ///< altitude for segment
      teAltitudeMode meAltitudeMode;   ///< altitude mode 
      teGuidanceMode meGuidanceMode;   ///< guidance mode 
   };

#define MAX_MISSILE_FLIGHT_SEGMENTS 8


   class tcMissileDBObject : public tcWeaponDBObject, public tcAirDetectionDBObject
   {
   public:
      // flight model parameters
      float mfDragArea_sm;                ///< area for parasitic drag 这是用于寄生阻力的面积。寄生阻力是与物体形状和大小有关的阻力，不包括由于空气动力产生的推力
      float mfGmax;                       ///< max Gs 这是最大重力加速度，通常用于描述飞行器可以承受的最大过载
      float mfMaxTurnRate_degps;          ///< max (slow speed) turn rate 这是最大（低速）的旋转速率，以度每秒（degrees per second）为单位
      float mfCdpsub;                     ///< parasitic drag coeff, subsonic 这是亚音速的寄生阻力系数。
      float mfCdptran;                    ///< transonic 这是跨音速的寄生阻力系数。当飞行器在接近音速时，其阻力特性会发生变化。
      float mfCdpsup;                     ///< supersonic 这是超音速的寄生阻力系数。
      float mfMcm;                        ///< critical mach number 临界马赫数，这是描述飞行器或物体在某一速度下从亚音速过渡到超音速的马赫数。
      float mfMsupm;                      ///< supersonic mach number 超音速马赫数。描述飞行器或物体在超音速下的速度特性。
      float mfBoostThrust_N;              ///< boost thrust [N] 助推推力，以牛顿（N）为单位。在某些情况下，如火箭或某些导弹，在发射阶段需要更大的推力来达到所需的速度。
      float mfBoostTime_s;                ///< boost time [s] 助推时间，以秒为单位。描述助推阶段持续的时间长度。
      float mfSustThrust_N;               ///< sustainer thrust [N] 维持推力，以牛顿为单位。在达到所需速度后，可能需要较小的推力来维持飞行或推进。
      float mfSustTime_s;                 ///< sustainer time [s] 维持时间，以秒为单位。描述维持阶段持续的时间长度。
      float mfShutdownSpeed_mps;          ///< self destructs below this speed after flameout 在失去动力（flameout）后，飞行器或物体将在低于此速度时自动销毁或采取其他行动。这可能是为了防止故障或失去控制的飞行器造成损害。

      // other parameters
      //float mfDamage;                   ///< damage value
      //teDamageType meDamageType;        ///< damage type enumeration
      //float mfRange_km;                   ///< [km] nominal range (replaced with maxRange_km in tcWeaponDBObject
    
      // sensor info
      tcDBString maSensorClass;           ///< seeker database class name
      long sensorKey;                     ///< key for fast access of primary seeker
	  bool needsFireControl;              ///< true if seeker depends on a fire control sensor for guidance
      bool acceptsWaypoints;              ///< true if missile can accept preplan (or datalink) waypoints

	  int fireAndForget;				  ///< -1 not initialized, 0 not FF, 1 FF
      int isARM;                          ///< -1 not initialized, 0 not ARM, 1 ARM

      float seekerFOV_rad;                ///< for fast lookup of seeker field of view
      float aczConstant_kts;
      float invMass_kg;                   ///< 1/mass_kg to avoid divide

      /// flight profile, array of flight segment info
      unsigned mnNumSegments;
      std::array<tsMissileFlightSegment,MAX_MISSILE_FLIGHT_SEGMENTS>  maFlightProfile;

      virtual const char* GetClassName() const {return "Missile";} ///< returns class name of database object
      teWeaponLaunchMode GetLaunchMode() const;
      long GetSensorKey();
      float GetSeekerFOV(); ///< @returns FOV in radians
	  bool HasAllEmitters(std::vector<long>& emitters);
	  bool IsFireAndForget();
      bool IsCommandLaunched() const;
      bool IsARM();
	  bool NeedsFireControl() const;
      bool AcceptsWaypoints() const;
      float EstimateSpeed_mps() const;
      virtual void PrintToFile(tcFile& file);

	  static void AddSqlColumns(std::string& columnString);
	  void ReadSql(tcSqlReader& entry);
      void WriteSql(std::string& valueString) const;

      void CalculateParams();

      tcMissileDBObject();
      tcMissileDBObject(const tcMissileDBObject& obj); ///< copy constructor
      virtual ~tcMissileDBObject();
      virtual  tcGameObject *CreateGameObject() override;

   };

}

#endif

