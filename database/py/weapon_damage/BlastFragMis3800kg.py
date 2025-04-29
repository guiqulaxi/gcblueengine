# -*- coding: utf-8 -*-
import pygcb
def CreateDBObject():
    dbObj=pygcb.tcWeaponDamage()
    dbObj.databaseClass='BlastFragMis3800kg'
    dbObj.maxRange_m=11227.031250
    dbObj.probDetonate=0.850000
    dbObj.blastCharge_kg=367.492737
    dbObj.fragCharge_kg=1959.004883
    dbObj.radCharge_kg=36.749275
    dbObj.fragMetal_kg=1473.502441
    dbObj.fragFragment_kg=0.411938
    dbObj.fragSpread=0.300000
    return dbObj
