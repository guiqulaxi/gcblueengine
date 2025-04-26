# -*- coding: utf-8 -*-
import pygcb
def CreateDBObject():
    dbObj=pygcb.tcWeaponDamage()
    dbObj.databaseClass='BlastFragAir385kg'
    dbObj.maxRange_m=5075.684082
    dbObj.probDetonate=0.850000
    dbObj.blastCharge_kg=58.972359
    dbObj.fragCharge_kg=183.985092
    dbObj.radCharge_kg=5.897236
    dbObj.fragMetal_kg=142.042542
    dbObj.fragFragment_kg=0.072323
    dbObj.fragSpread=0.300000
    return dbObj
