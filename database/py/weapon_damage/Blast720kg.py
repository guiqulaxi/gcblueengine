# -*- coding: utf-8 -*-
import pygcb
def CreateDBObject():
    dbObj=pygcb.tcWeaponDamage()
    dbObj.databaseClass='Blast720kg'
    dbObj.maxRange_m=110.848221
    dbObj.probDetonate=0.850000
    dbObj.blastCharge_kg=700.000000
    dbObj.fragCharge_kg=0.000000
    dbObj.radCharge_kg=70.000000
    dbObj.fragMetal_kg=0.000000
    dbObj.fragFragment_kg=0.000000
    dbObj.fragSpread=0.000000
    return dbObj
