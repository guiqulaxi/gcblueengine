# -*- coding: utf-8 -*-
import pygcb
def CreateDBObject():
    dbObj=pygcb.tcWeaponDamage()
    dbObj.databaseClass='BlastFrag23.5kg'
    dbObj.maxRange_m=870.212097
    dbObj.probDetonate=0.850000
    dbObj.blastCharge_kg=8.382139
    dbObj.fragCharge_kg=7.336907
    dbObj.radCharge_kg=0.838214
    dbObj.fragMetal_kg=7.780954
    dbObj.fragFragment_kg=0.002601
    dbObj.fragSpread=0.300000
    return dbObj
