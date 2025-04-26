# -*- coding: utf-8 -*-
import pygcb
def CreateDBObject():
    dbObj=pygcb.tcWeaponDamage()
    dbObj.databaseClass='Pen46kg'
    dbObj.maxRange_m=39.758228
    dbObj.probDetonate=0.850000
    dbObj.blastCharge_kg=32.200001
    dbObj.fragCharge_kg=0.000000
    dbObj.radCharge_kg=4.600000
    dbObj.fragMetal_kg=0.000000
    dbObj.fragFragment_kg=0.000000
    dbObj.fragSpread=0.000000
    return dbObj
