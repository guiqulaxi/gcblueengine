/** 
**  @file tcMatrix3.cpp
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

#include "tcMatrix3.h"
//#include "stdwx.h"

#ifndef WX_PRECOMP
////#include "wx/wx.h" 
#endif

#ifdef _DEBUG
#define new DEBUG_NEW
#endif



Matrix3d& tcMatrix3::GetMatrix()
{
    return matrix;
}

const Vector3d& tcMatrix3::PreMultiply(Vector3d& v)
{
    tcMatrix3 transpose;

    //math.TVMatrixTranspose(transpose.GetMatrix(), GetMatrix());

    return transpose.operator*(v);

}

/**
* Update this matrix as M = m*M and return ref to this matrix
*/
const tcMatrix3& tcMatrix3::PreMultiply(tcMatrix3& m)
{
    // void TVMatrixMultiply(cTV_3DMATRIX* retOutMatrix, cTV_3DMATRIX* mMat1, cTV_3DMATRIX* mMat2);
//    tcMatrix3 result;
//    math.TVMatrixMultiply(result.GetMatrix(), m.GetMatrix(), GetMatrix());
//    *this = result;

    matrix=matrix*m.GetMatrix();
    return *this;
}


void tcMatrix3::Test()
{
    fprintf(stdout, "--- tcMatrix3::Test() ---\n");
    static tcMatrix3 T;

    Vector3d x(1, 1, 1);
    T.SetYawPitchRoll(0.5, 0, 0);

    Vector3d y = T*x;

    fprintf(stdout, "x: (%f, %f, %f) -> y: (%f, %f, %f)\n", x.x(), x.y(), x.z(), y.x(), y.y(), y.z());
}

void tcMatrix3::SetInverseYawPitchRoll(float yaw_rad, float pitch_rad, float roll_rad)
{
    Eigen::Quaterniond quaternion;
    quaternion =    Eigen::AngleAxisd(yaw_rad, Eigen::Vector3d::UnitZ()) *
            Eigen::AngleAxisd(pitch_rad, Eigen::Vector3d::UnitX()) *
            Eigen::AngleAxisd(roll_rad, Eigen::Vector3d::UnitY());
    matrix=quaternion.inverse().matrix();

//    cTV_3DMATRIX temp;
//    math.TVMatrixRotationYawPitchRoll(&temp, yaw_rad, pitch_rad, roll_rad);

//    float det;
//    math.TVMatrixInverse(&m, &det, &temp);

//    matrix.makeRotate(yaw_rad,Vector3d(0.0f, 1.0f, 0.0f) ); // 以 Y 轴为旋转轴，旋转 Yaw 度
//    matrix.makeRotate(pitch_rad,Vector3d(1.0f, 0.0f, 0.0f)); // 以 X 轴为旋转轴，旋转 Pitch 度
//    matrix.makeRotate(roll_rad,Vector3d(0.0f, 0.0f, 1.0f)); // 以 Z 轴为旋转轴，旋转 Roll 度
//    Matrix3d m;
//    matrix.inverse(m);
//    matrix=m;
}

void tcMatrix3::SetYawPitchRoll(float yaw_rad, float pitch_rad, float roll_rad)
{

    //math.TVMatrixRotationYawPitchRoll(&m, yaw_rad, pitch_rad, roll_rad);

//    matrix.makeRotate(yaw_rad,osg::Vector3d(0.0f, 1.0f, 0.0f) ); // 以 Y 轴为旋转轴，旋转 Yaw 度
//    matrix.makeRotate(pitch_rad,osg::Vector3d(1.0f, 0.0f, 0.0f)); // 以 X 轴为旋转轴，旋转 Pitch 度
//    matrix.makeRotate(roll_rad,osg::Vector3d(0.0f, 0.0f, 1.0f)); // 以 Z 轴为旋转轴，旋转 Roll 度
    Eigen::Quaterniond quaternion;
    quaternion =    Eigen::AngleAxisd(yaw_rad, Eigen::Vector3d::UnitZ()) *
            Eigen::AngleAxisd(pitch_rad, Eigen::Vector3d::UnitX()) *
            Eigen::AngleAxisd(roll_rad, Eigen::Vector3d::UnitY());
    matrix=quaternion.matrix();
}

const Vector3d& tcMatrix3::operator*(Vector3d& v)
{
    static Vector3d result;
    result=matrix*v;
    //math.TVVector3dTransformCoord(&result, &v, &m);
    return result;
}

tcMatrix3::tcMatrix3()
{
  matrix.setZero();
}

tcMatrix3::~tcMatrix3()
{
}
