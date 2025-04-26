# -*- coding: utf-8 -*-
import pygcb
def CreateDBObject():
    dbObj=pygcb.tcWeaponDamage()
    dbObj.databaseClass='BlastFragMis26kg'
    dbObj.maxRange_m=3048.053955
    dbObj.probDetonate=0.850000
    dbObj.blastCharge_kg=5.710782
    dbObj.fragCharge_kg=11.272812
    dbObj.radCharge_kg=0.571078
    dbObj.fragMetal_kg=9.016406
    dbObj.fragFragment_kg=0.025185
    dbObj.fragSpread=0.247230
    return dbObj
