# -*- coding: utf-8 -*-
import pygcb
def CreateDBObject():
    dbObj=pygcb.tcWeaponDamage()
    dbObj.databaseClass='Nuclear-2900kT'
    dbObj.maxRange_m=43729.992188
    dbObj.probDetonate=0.900000
    dbObj.blastCharge_kg=3190000128.000000
    dbObj.fragCharge_kg=0.000000
    dbObj.radCharge_kg=1450000000.000000
    dbObj.fragMetal_kg=0.000000
    dbObj.fragFragment_kg=0.000000
    dbObj.fragSpread=1.000000
    return dbObj
