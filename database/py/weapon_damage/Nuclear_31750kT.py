# -*- coding: utf-8 -*-
import pygcb
def CreateDBObject():
    dbObj=pygcb.tcWeaponDamage()
    dbObj.databaseClass='Nuclear-31750kT'
    dbObj.maxRange_m=89656.773438
    dbObj.probDetonate=0.900000
    dbObj.blastCharge_kg=34924998656.000000
    dbObj.fragCharge_kg=0.000000
    dbObj.radCharge_kg=15875000320.000000
    dbObj.fragMetal_kg=0.000000
    dbObj.fragFragment_kg=0.000000
    dbObj.fragSpread=1.000000
    return dbObj
