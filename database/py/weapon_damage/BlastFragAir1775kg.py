# -*- coding: utf-8 -*-
import pygcb
def CreateDBObject():
    dbObj=pygcb.tcWeaponDamage()
    dbObj.databaseClass='BlastFragAir1775kg'
    dbObj.maxRange_m=8487.196289
    dbObj.probDetonate=0.850000
    dbObj.blastCharge_kg=204.980789
    dbObj.fragCharge_kg=892.846130
    dbObj.radCharge_kg=20.498079
    dbObj.fragMetal_kg=677.173096
    dbObj.fragFragment_kg=0.220578
    dbObj.fragSpread=0.300000
    return dbObj
