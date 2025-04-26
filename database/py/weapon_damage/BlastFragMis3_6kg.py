# -*- coding: utf-8 -*-
import pygcb
def CreateDBObject():
    dbObj=pygcb.tcWeaponDamage()
    dbObj.databaseClass='BlastFragMis3.6kg'
    dbObj.maxRange_m=1538.677368
    dbObj.probDetonate=0.850000
    dbObj.blastCharge_kg=0.966270
    dbObj.fragCharge_kg=1.443820
    dbObj.radCharge_kg=0.096627
    dbObj.fragMetal_kg=1.189910
    dbObj.fragFragment_kg=0.006685
    dbObj.fragSpread=0.061119
    return dbObj
