/**  
**  @file tcBoundingBox.cpp
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

#include "tcAABBBoundingBox.h"

#ifdef _DEBUG
#define new DEBUG_NEW
#endif 
tcAABBBoundingBox::tcAABBBoundingBox(const Vector3d &center_,
                          const Vector3d &extents_,
                          double yaw_,
                          double roll_,
                          double pitch_):
   center(center_),
   extents(extents_),
   yaw(yaw_),
   roll(roll_),
   pitch(pitch_)
{
calcAttributes();
}

void tcAABBBoundingBox::Set(const Vector3d &center_,
                          const Vector3d &extents_,
                          double yaw_,
                          double roll_,
                          double pitch_)
{
   center=center_;
   extents=extents_;
   yaw=yaw_;
   roll=roll_;
   pitch=pitch_;
   calcAttributes();
}

double tcAABBBoundingBox::zmin() const
{
    return pmin.z();
}

double tcAABBBoundingBox::zmax() const
{
    return pmax.z();
}


tcAABBBoundingBox::tcAABBBoundingBox(const tcAABBBoundingBox& src)
    :
       center(src.center),
       extents(src.extents),
       yaw(src.yaw),
       roll(src.roll),
       pitch(src.pitch)
{

}

tcAABBBoundingBox::tcAABBBoundingBox()
{
}

tcAABBBoundingBox::~tcAABBBoundingBox()
{
}

void tcAABBBoundingBox::calcAttributes()
{
    Eigen::Quaterniond quaternion;
    //沿着正方向逆时针转
    quaternion =Eigen::AngleAxisd(yaw, Eigen::Vector3d::UnitZ()) *
            Eigen::AngleAxisd(roll, Eigen::Vector3d::UnitZ()) *
            Eigen::AngleAxisd(pitch, Eigen::Vector3d::UnitY());
    Vector3d p_1=quaternion*Vector3d(extents.array()*Vector3d(1,1,1).array())+center;
    Vector3d p_2=quaternion*Vector3d(extents.array()*Vector3d(-1,1,1).array())+center;
    Vector3d p_3=quaternion*Vector3d(extents.array()*Vector3d(1,-1,1).array())+center;
    Vector3d p_4=quaternion*Vector3d(extents.array()*Vector3d(1,1,-1).array())+center;
    Vector3d p_5=quaternion*Vector3d(extents.array()*Vector3d(1,-1,-1).array())+center;
    Vector3d p_6=quaternion*Vector3d(extents.array()*Vector3d(-1,1,-1).array())+center;
    Vector3d p_7=quaternion*Vector3d(extents.array()*Vector3d(-1,-1,1).array())+center;
    Vector3d p_8=quaternion*Vector3d(extents.array()*Vector3d(-1,-1,-1).array())+center;

    std::vector ps={p_2,p_3,p_4,p_5,p_6,p_7,p_8};
    pmax=p_1;
    pmin=p_1;
    for(Vector3d &v :ps)
    {
       pmin.x()=std::min(pmin.x(),v.x());
       pmin.y()=std::min(pmin.y(),v.y());
       pmin.z()=std::min(pmin.z(),v.z());
       pmax.x()=std::min(pmax.x(),v.x());
       pmax.y()=std::min(pmax.y(),v.y());
       pmax.z()=std::min(pmax.z(),v.z());
    }

}
