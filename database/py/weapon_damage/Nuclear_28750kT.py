# -*- coding: utf-8 -*-
import pygcb
def CreateDBObject():
    dbObj=pygcb.tcWeaponDamage()
    dbObj.databaseClass='Nuclear-28750kT'
    dbObj.maxRange_m=87026.468750
    dbObj.probDetonate=0.900000
    dbObj.blastCharge_kg=31625000960.000000
    dbObj.fragCharge_kg=0.000000
    dbObj.radCharge_kg=14375000064.000000
    dbObj.fragMetal_kg=0.000000
    dbObj.fragFragment_kg=0.000000
    dbObj.fragSpread=1.000000
    return dbObj
