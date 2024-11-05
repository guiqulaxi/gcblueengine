/**  
**  @file tcBoundingBox.h
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

#ifndef _TCOBBBOUNDINGBOX_
#define _TCOBBBOUNDINGBOX_

#if _MSC_VER > 1000
#pragma once
#endif 

////#include "tv_types.h"
#include <Dense>
using Eigen::Vector3d;
/**
*
*/
class tcOBBBoundingBox
{
public:
    tcOBBBoundingBox();
     tcOBBBoundingBox(const Vector3d& center, const Vector3d& extents,
                      double yaw,double roll,double pitch);
    /**
     * @brief Set
     * @param center 中心点
     * @param extents 包围盒在每个方向上的半尺寸 y  长（x）、宽（y）、高(z)
     * @param yaw 弧度
     * @param roll 弧度
     * @param pitch 弧度
     */
    void Set(const Vector3d& center, const Vector3d& extents,
             double yaw,double roll,double pitch);


    tcOBBBoundingBox(const tcOBBBoundingBox& src);

    virtual ~tcOBBBoundingBox();
    //获得八个顶点
    std::vector<Vector3d> GetCorners() const;
    std::vector<std::vector<Vector3d>> GetPlanes() const;
    double zmin() const;
    double zmax() const;
private:
    //计算属性
    void calcAttributes();
    Vector3d center; // 包围盒的中心点
    Vector3d extents; // 包围盒在每个方向上的半尺寸
   //x right, y forward , z up
    double yaw;//绕z轴旋转， 弧度
    double roll;// 绕y轴旋转，弧度
    double pitch;//绕x轴旋转，弧度
    //平面
    std::vector<std::vector<Vector3d>>  planes;
    //顶点
    std::vector<Vector3d>  corners;

    Vector3d pmax;
    Vector3d pmin;
};

#endif
