# -*- coding: utf-8 -*-
import pygcb
def CreateDBObject():
    dbObj=pygcb.tcWeaponDamage()
    dbObj.databaseClass='Pen28kg'
    dbObj.maxRange_m=33.700191
    dbObj.probDetonate=0.850000
    dbObj.blastCharge_kg=19.600000
    dbObj.fragCharge_kg=0.000000
    dbObj.radCharge_kg=2.800000
    dbObj.fragMetal_kg=0.000000
    dbObj.fragFragment_kg=0.000000
    dbObj.fragSpread=0.000000
    return dbObj
