# -*- coding: utf-8 -*-
import pygcb
def CreateDBObject():
    dbObj=pygcb.tcWeaponDamage()
    dbObj.databaseClass='BlastFrag3300kg'
    dbObj.maxRange_m=7328.964355
    dbObj.probDetonate=0.850000
    dbObj.blastCharge_kg=1187.800171
    dbObj.fragCharge_kg=1023.133179
    dbObj.radCharge_kg=118.780022
    dbObj.fragMetal_kg=1089.066650
    dbObj.fragFragment_kg=0.169320
    dbObj.fragSpread=0.300000
    return dbObj
