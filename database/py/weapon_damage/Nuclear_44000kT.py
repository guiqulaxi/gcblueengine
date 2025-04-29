# -*- coding: utf-8 -*-
import pygcb
def CreateDBObject():
    dbObj=pygcb.tcWeaponDamage()
    dbObj.databaseClass='Nuclear-44000kT'
    dbObj.maxRange_m=98877.117188
    dbObj.probDetonate=0.900000
    dbObj.blastCharge_kg=48399998976.000000
    dbObj.fragCharge_kg=0.000000
    dbObj.radCharge_kg=22000001024.000000
    dbObj.fragMetal_kg=0.000000
    dbObj.fragFragment_kg=0.000000
    dbObj.fragSpread=1.000000
    return dbObj
