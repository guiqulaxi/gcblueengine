# -*- coding: utf-8 -*-
import pygcb
def CreateDBObject():
    dbObj=pygcb.tcWeaponDamage()
    dbObj.databaseClass='Nuclear-13750kT'
    dbObj.maxRange_m=69751.054688
    dbObj.probDetonate=0.900000
    dbObj.blastCharge_kg=15125000192.000000
    dbObj.fragCharge_kg=0.000000
    dbObj.radCharge_kg=6874999808.000000
    dbObj.fragMetal_kg=0.000000
    dbObj.fragFragment_kg=0.000000
    dbObj.fragSpread=1.000000
    return dbObj
