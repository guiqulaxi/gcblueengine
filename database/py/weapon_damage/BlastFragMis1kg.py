# -*- coding: utf-8 -*-
import pygcb
def CreateDBObject():
    dbObj=pygcb.tcWeaponDamage()
    dbObj.databaseClass='BlastFragMis1kg'
    dbObj.maxRange_m=779.824890
    dbObj.probDetonate=0.850000
    dbObj.blastCharge_kg=0.300000
    dbObj.fragCharge_kg=0.380000
    dbObj.radCharge_kg=0.030000
    dbObj.fragMetal_kg=0.320000
    dbObj.fragFragment_kg=0.002025
    dbObj.fragSpread=0.048156
    return dbObj
