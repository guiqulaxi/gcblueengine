# -*- coding: utf-8 -*-
import pygcb
def CreateDBObject():
    dbObj=pygcb.tcWeaponDamage()
    dbObj.databaseClass='Blast960kg'
    dbObj.maxRange_m=123.142342
    dbObj.probDetonate=0.850000
    dbObj.blastCharge_kg=960.000000
    dbObj.fragCharge_kg=0.000000
    dbObj.radCharge_kg=96.000000
    dbObj.fragMetal_kg=0.000000
    dbObj.fragFragment_kg=0.000000
    dbObj.fragSpread=0.000000
    return dbObj
