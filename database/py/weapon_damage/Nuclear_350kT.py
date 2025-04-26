# -*- coding: utf-8 -*-
import pygcb
def CreateDBObject():
    dbObj=pygcb.tcWeaponDamage()
    dbObj.databaseClass='Nuclear-350kT'
    dbObj.maxRange_m=23188.914062
    dbObj.probDetonate=0.900000
    dbObj.blastCharge_kg=385000000.000000
    dbObj.fragCharge_kg=0.000000
    dbObj.radCharge_kg=175000000.000000
    dbObj.fragMetal_kg=0.000000
    dbObj.fragFragment_kg=0.000000
    dbObj.fragSpread=1.000000
    return dbObj
