# -*- coding: utf-8 -*-
import pygcb
def CreateDBObject():
    dbObj=pygcb.tcWeaponDamage()
    dbObj.databaseClass='Nuclear-23500kT'
    dbObj.maxRange_m=81918.187500
    dbObj.probDetonate=0.900000
    dbObj.blastCharge_kg=25849999360.000000
    dbObj.fragCharge_kg=0.000000
    dbObj.radCharge_kg=11749999616.000000
    dbObj.fragMetal_kg=0.000000
    dbObj.fragFragment_kg=0.000000
    dbObj.fragSpread=1.000000
    return dbObj
