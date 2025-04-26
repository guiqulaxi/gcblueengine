# -*- coding: utf-8 -*-
import pygcb
def CreateDBObject():
    dbObj=pygcb.tcWeaponDamage()
    dbObj.databaseClass='Pen3650kg'
    dbObj.maxRange_m=170.597336
    dbObj.probDetonate=0.850000
    dbObj.blastCharge_kg=2555.000000
    dbObj.fragCharge_kg=0.000000
    dbObj.radCharge_kg=365.000000
    dbObj.fragMetal_kg=0.000000
    dbObj.fragFragment_kg=0.000000
    dbObj.fragSpread=0.000000
    return dbObj
