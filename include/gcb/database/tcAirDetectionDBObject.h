/**
**  @file tcAirDetectionDBObject.h
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

#ifndef _AIRDETECTIONDBOBJECT_H_
#define _AIRDETECTIONDBOBJECT_H_

#include "tcSignatureModel.h"
#if _MSC_VER > 1000
#pragma once
#endif // _MSC_VER > 1000

#include <string>
#include <memory>
namespace database
{
	class tcSqlReader;
    class tcSignatureModel;

    /**
    * Describes detectability of object through air via radar, optical,
	* and IR.
    */
    class tcAirDetectionDBObject: public std::enable_shared_from_this<tcAirDetectionDBObject>
    {
    public:
        enum {IRMODELA = 0, IRMODELB = 1, IRMODELC = 2};
        
        float RCS_dBsm;						///< base radar cross section, [dBsm] 基本雷达散射截面
        std::string RCS_Model;              ///< aspect variation model 雷达散射截面随角度变化的模型
        float opticalCrossSection_dBsm;	    ///< 光学散射截面，单位为分贝平方米
        float irSignature_dB;			    ///< IR emissions for passive IR detection
        std::string IR_ModelA;              ///< basic model 基本红外特征模型 用于被动红外探测的红外发射强度
        std::string IR_ModelB;              ///< ADDITIONAL signature for afterburners 加力燃烧后的附加红外特征
        std::string IR_ModelC;              ///< signature for supersonic flight 超音速飞行时的红外特征
        float effectiveHeight_m;            ///< effective height for horizon test 用于地平线测试的有效高度，单位为米

        tcSignatureModel radarSignature;
        tcSignatureModel irSignatureA;
        tcSignatureModel irSignatureB;
        tcSignatureModel irSignatureC;

		static void AddSqlColumns(std::string& columnString);
		void ReadSql(tcSqlReader& entry);
        void WriteSql(std::string& valueString) const;
        void WritePythonValue(const std::string& mzClass,std::string& valueString) const;
         void WritePython(const std::string& mzClass,std::string& valueString) const;
        float GetRCS_dBsm(float az_deg) const;
        float GetIRSig_dB(float az_deg, int irModel) const;

        tcAirDetectionDBObject();
        tcAirDetectionDBObject(const tcAirDetectionDBObject& obj); ///< copy constructor
        virtual ~tcAirDetectionDBObject();


    
        void BindSignatureModels();
    };

}

#endif

