# -*- coding: utf-8 -*-
import pygcb
def CreateDBObject():
    dbObj=pygcb.tcWeaponDamage()
    dbObj.databaseClass='Nuclear-43000kT'
    dbObj.maxRange_m=98197.523438
    dbObj.probDetonate=0.900000
    dbObj.blastCharge_kg=47300001792.000000
    dbObj.fragCharge_kg=0.000000
    dbObj.radCharge_kg=21500000256.000000
    dbObj.fragMetal_kg=0.000000
    dbObj.fragFragment_kg=0.000000
    dbObj.fragSpread=1.000000
    return dbObj
