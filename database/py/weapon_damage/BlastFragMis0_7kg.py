# -*- coding: utf-8 -*-
import pygcb
def CreateDBObject():
    dbObj=pygcb.tcWeaponDamage()
    dbObj.databaseClass='BlastFragMis0.7kg'
    dbObj.maxRange_m=633.480286
    dbObj.probDetonate=0.850000
    dbObj.blastCharge_kg=0.210000
    dbObj.fragCharge_kg=0.266000
    dbObj.radCharge_kg=0.021000
    dbObj.fragMetal_kg=0.224000
    dbObj.fragFragment_kg=0.001445
    dbObj.fragSpread=0.046345
    return dbObj
