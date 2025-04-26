# -*- coding: utf-8 -*-
import pygcb
def CreateDBObject():
    dbObj=pygcb.tcWeaponDamage()
    dbObj.databaseClass='Pen1225kg'
    dbObj.maxRange_m=118.598190
    dbObj.probDetonate=0.850000
    dbObj.blastCharge_kg=857.500000
    dbObj.fragCharge_kg=0.000000
    dbObj.radCharge_kg=122.500000
    dbObj.fragMetal_kg=0.000000
    dbObj.fragFragment_kg=0.000000
    dbObj.fragSpread=0.000000
    return dbObj
