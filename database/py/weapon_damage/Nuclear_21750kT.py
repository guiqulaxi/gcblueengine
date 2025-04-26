# -*- coding: utf-8 -*-
import pygcb
def CreateDBObject():
    dbObj=pygcb.tcWeaponDamage()
    dbObj.databaseClass='Nuclear-21750kT'
    dbObj.maxRange_m=80038.281250
    dbObj.probDetonate=0.900000
    dbObj.blastCharge_kg=23925000192.000000
    dbObj.fragCharge_kg=0.000000
    dbObj.radCharge_kg=10874999808.000000
    dbObj.fragMetal_kg=0.000000
    dbObj.fragFragment_kg=0.000000
    dbObj.fragSpread=1.000000
    return dbObj
