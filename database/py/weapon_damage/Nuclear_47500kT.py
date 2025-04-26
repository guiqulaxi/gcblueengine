# -*- coding: utf-8 -*-
import pygcb
def CreateDBObject():
    dbObj=pygcb.tcWeaponDamage()
    dbObj.databaseClass='Nuclear-47500kT'
    dbObj.maxRange_m=101173.804688
    dbObj.probDetonate=0.900000
    dbObj.blastCharge_kg=52250001408.000000
    dbObj.fragCharge_kg=0.000000
    dbObj.radCharge_kg=23750000640.000000
    dbObj.fragMetal_kg=0.000000
    dbObj.fragFragment_kg=0.000000
    dbObj.fragSpread=1.000000
    return dbObj
