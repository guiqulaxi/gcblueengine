# -*- coding: utf-8 -*-
import pygcb
def CreateDBObject():
    dbObj=pygcb.tcWeaponDamage()
    dbObj.databaseClass='BlastFragMis3700kg'
    dbObj.maxRange_m=11126.678711
    dbObj.probDetonate=0.850000
    dbObj.blastCharge_kg=360.255432
    dbObj.fragCharge_kg=1905.829712
    dbObj.radCharge_kg=36.025543
    dbObj.fragMetal_kg=1433.914795
    dbObj.fragFragment_kg=0.403692
    dbObj.fragSpread=0.300000
    return dbObj
