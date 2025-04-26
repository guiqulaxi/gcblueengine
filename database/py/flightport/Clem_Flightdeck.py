# -*- coding: utf-8 -*-
import pygcb
def CreateDBObject():
    dbObj=pygcb.tcFlightportDBObject()
    dbObj.mzClass='Clem Flightdeck'
    dbObj.natoClass='Clem Flightdeck'
    dbObj.mnModelType=0
    dbObj.mnType=0
    dbObj.cost=0.000000
    dbObj.weight_kg=0.000000
    dbObj.volume_m3=0.000000
    dbObj.initialYear=1900.000000
    dbObj.finalYear=2999.000000
    dbObj.country=''
    dbObj.designation=''
    dbObj.imageList=''
    dbObj.iconFileName=''
    dbObj.mz3DModelFileName=''
    dbObj.notes='boosted from 0 to 3000 m length until aircraft lengths sorted out'
    dbObj.length_m=1.000000
    dbObj.width_m=1.000000
    dbObj.height_m=1.000000
    dbObj.heloOnly=0
    dbObj.hangarCapacity=40
    dbObj.spotInfo=[pygcb.spotDBInfo()]*4
    dbObj.spotInfo[0].isLaunch=1
    dbObj.spotInfo[0].x=-12.500000
    dbObj.spotInfo[0].y=-18.799999
    dbObj.spotInfo[0].z=16.000000
    dbObj.spotInfo[0].orientation_deg=2.500000
    dbObj.spotInfo[0].length=3000.000000
    dbObj.spotInfo[1].isLaunch=1
    dbObj.spotInfo[1].x=-2.500000
    dbObj.spotInfo[1].y=-18.799999
    dbObj.spotInfo[1].z=16.000000
    dbObj.spotInfo[1].orientation_deg=-2.000000
    dbObj.spotInfo[1].length=3000.000000
    dbObj.spotInfo[2].isLaunch=0
    dbObj.spotInfo[2].x=5.000000
    dbObj.spotInfo[2].y=-36.250000
    dbObj.spotInfo[2].z=16.000000
    dbObj.spotInfo[2].orientation_deg=-30.000000
    dbObj.spotInfo[2].length=0.000000
    dbObj.spotInfo[3].isLaunch=0
    dbObj.spotInfo[3].x=1.250000
    dbObj.spotInfo[3].y=-45.000000
    dbObj.spotInfo[3].z=16.000000
    dbObj.spotInfo[3].orientation_deg=-30.000000
    dbObj.spotInfo[3].length=0.000000
    dbObj.CalculateParams()
    return dbObj
