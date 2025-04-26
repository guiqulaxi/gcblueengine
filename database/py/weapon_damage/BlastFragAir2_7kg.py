# -*- coding: utf-8 -*-
import pygcb
def CreateDBObject():
    dbObj=pygcb.tcWeaponDamage()
    dbObj.databaseClass='BlastFragAir2.7kg'
    dbObj.maxRange_m=1339.431763
    dbObj.probDetonate=0.850000
    dbObj.blastCharge_kg=0.743859
    dbObj.fragCharge_kg=1.070094
    dbObj.radCharge_kg=0.074386
    dbObj.fragMetal_kg=0.886047
    dbObj.fragFragment_kg=0.005182
    dbObj.fragSpread=0.056406
    return dbObj
