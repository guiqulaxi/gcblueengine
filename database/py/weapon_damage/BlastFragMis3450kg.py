# -*- coding: utf-8 -*-
import pygcb
def CreateDBObject():
    dbObj=pygcb.tcWeaponDamage()
    dbObj.databaseClass='BlastFragMis3450kg'
    dbObj.maxRange_m=10864.969727
    dbObj.probDetonate=0.850000
    dbObj.blastCharge_kg=341.866455
    dbObj.fragCharge_kg=1773.088989
    dbObj.radCharge_kg=34.186646
    dbObj.fragMetal_kg=1335.044556
    dbObj.fragFragment_kg=0.382644
    dbObj.fragSpread=0.300000
    return dbObj
