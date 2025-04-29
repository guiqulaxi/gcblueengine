# -*- coding: utf-8 -*-
import pygcb
def CreateDBObject():
    dbObj=pygcb.tcWeaponDamage()
    dbObj.databaseClass='Nuclear-3kT'
    dbObj.maxRange_m=5561.556641
    dbObj.probDetonate=0.900000
    dbObj.blastCharge_kg=3300000.000000
    dbObj.fragCharge_kg=0.000000
    dbObj.radCharge_kg=1500000.000000
    dbObj.fragMetal_kg=0.000000
    dbObj.fragFragment_kg=0.000000
    dbObj.fragSpread=1.000000
    return dbObj
