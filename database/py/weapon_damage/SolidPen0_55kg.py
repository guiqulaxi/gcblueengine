# -*- coding: utf-8 -*-
import pygcb
def CreateDBObject():
    dbObj=pygcb.tcWeaponDamage()
    dbObj.databaseClass='SolidPen0.55kg'
    dbObj.maxRange_m=34.446941
    dbObj.probDetonate=1.000000
    dbObj.blastCharge_kg=0.550000
    dbObj.fragCharge_kg=0.000000
    dbObj.radCharge_kg=0.000000
    dbObj.fragMetal_kg=0.000000
    dbObj.fragFragment_kg=0.000000
    dbObj.fragSpread=1.000000
    return dbObj
