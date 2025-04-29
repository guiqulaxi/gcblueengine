# -*- coding: utf-8 -*-
import pygcb
def CreateDBObject():
    dbObj=pygcb.tcWeaponDamage()
    dbObj.databaseClass='Nuclear-21000kT'
    dbObj.maxRange_m=79200.109375
    dbObj.probDetonate=0.900000
    dbObj.blastCharge_kg=23100000256.000000
    dbObj.fragCharge_kg=0.000000
    dbObj.radCharge_kg=10499999744.000000
    dbObj.fragMetal_kg=0.000000
    dbObj.fragFragment_kg=0.000000
    dbObj.fragSpread=1.000000
    return dbObj
