# -*- coding: utf-8 -*-
import pygcb
def CreateDBObject():
    dbObj=pygcb.tcWeaponDamage()
    dbObj.databaseClass='Blast3.7kg'
    dbObj.maxRange_m=19.342930
    dbObj.probDetonate=0.850000
    dbObj.blastCharge_kg=3.700000
    dbObj.fragCharge_kg=0.000000
    dbObj.radCharge_kg=0.370000
    dbObj.fragMetal_kg=0.000000
    dbObj.fragFragment_kg=0.000000
    dbObj.fragSpread=0.000000
    return dbObj
