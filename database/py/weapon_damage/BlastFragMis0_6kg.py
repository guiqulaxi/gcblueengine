# -*- coding: utf-8 -*-
import pygcb
def CreateDBObject():
    dbObj=pygcb.tcWeaponDamage()
    dbObj.databaseClass='BlastFragMis0.6kg'
    dbObj.maxRange_m=576.652039
    dbObj.probDetonate=0.850000
    dbObj.blastCharge_kg=0.180000
    dbObj.fragCharge_kg=0.228000
    dbObj.radCharge_kg=0.018000
    dbObj.fragMetal_kg=0.192000
    dbObj.fragFragment_kg=0.001247
    dbObj.fragSpread=0.045748
    return dbObj
