# -*- coding: utf-8 -*-
import pygcb
def CreateDBObject():
    dbObj=pygcb.tcWeaponDamage()
    dbObj.databaseClass='Pen38kg'
    dbObj.maxRange_m=37.307549
    dbObj.probDetonate=0.850000
    dbObj.blastCharge_kg=26.600000
    dbObj.fragCharge_kg=0.000000
    dbObj.radCharge_kg=3.800000
    dbObj.fragMetal_kg=0.000000
    dbObj.fragFragment_kg=0.000000
    dbObj.fragSpread=0.000000
    return dbObj
