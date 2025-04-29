# -*- coding: utf-8 -*-
import pygcb
def CreateDBObject():
    dbObj=pygcb.tcWeaponDamage()
    dbObj.databaseClass='BlastFragAir2150kg'
    dbObj.maxRange_m=9145.348633
    dbObj.probDetonate=0.850000
    dbObj.blastCharge_kg=238.123322
    dbObj.fragCharge_kg=1088.251099
    dbObj.radCharge_kg=23.812332
    dbObj.fragMetal_kg=823.625549
    dbObj.fragFragment_kg=0.260311
    dbObj.fragSpread=0.300000
    return dbObj
