# -*- coding: utf-8 -*-
import pygcb
def CreateDBObject():
    dbObj=pygcb.tcWeaponDamage()
    dbObj.databaseClass='Nuclear-4700kT'
    dbObj.maxRange_m=50546.296875
    dbObj.probDetonate=0.900000
    dbObj.blastCharge_kg=5169999872.000000
    dbObj.fragCharge_kg=0.000000
    dbObj.radCharge_kg=2350000128.000000
    dbObj.fragMetal_kg=0.000000
    dbObj.fragFragment_kg=0.000000
    dbObj.fragSpread=1.000000
    return dbObj
