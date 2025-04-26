# -*- coding: utf-8 -*-
import pygcb
def CreateDBObject():
    dbObj=pygcb.tcWeaponDamage()
    dbObj.databaseClass='Pen550kg'
    dbObj.maxRange_m=90.838409
    dbObj.probDetonate=0.850000
    dbObj.blastCharge_kg=385.000000
    dbObj.fragCharge_kg=0.000000
    dbObj.radCharge_kg=55.000000
    dbObj.fragMetal_kg=0.000000
    dbObj.fragFragment_kg=0.000000
    dbObj.fragSpread=0.000000
    return dbObj
