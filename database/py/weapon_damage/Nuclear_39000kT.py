# -*- coding: utf-8 -*-
import pygcb
def CreateDBObject():
    dbObj=pygcb.tcWeaponDamage()
    dbObj.databaseClass='Nuclear-39000kT'
    dbObj.maxRange_m=95362.882812
    dbObj.probDetonate=0.900000
    dbObj.blastCharge_kg=42900000768.000000
    dbObj.fragCharge_kg=0.000000
    dbObj.radCharge_kg=19499999232.000000
    dbObj.fragMetal_kg=0.000000
    dbObj.fragFragment_kg=0.000000
    dbObj.fragSpread=1.000000
    return dbObj
