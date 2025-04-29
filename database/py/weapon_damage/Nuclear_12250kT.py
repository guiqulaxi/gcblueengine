# -*- coding: utf-8 -*-
import pygcb
def CreateDBObject():
    dbObj=pygcb.tcWeaponDamage()
    dbObj.databaseClass='Nuclear-12250kT'
    dbObj.maxRange_m=67375.320312
    dbObj.probDetonate=0.900000
    dbObj.blastCharge_kg=13475000320.000000
    dbObj.fragCharge_kg=0.000000
    dbObj.radCharge_kg=6125000192.000000
    dbObj.fragMetal_kg=0.000000
    dbObj.fragFragment_kg=0.000000
    dbObj.fragSpread=1.000000
    return dbObj
