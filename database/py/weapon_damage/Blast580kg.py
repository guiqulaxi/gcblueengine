# -*- coding: utf-8 -*-
import pygcb
def CreateDBObject():
    dbObj=pygcb.tcWeaponDamage()
    dbObj.databaseClass='Blast580kg'
    dbObj.maxRange_m=104.119629
    dbObj.probDetonate=0.850000
    dbObj.blastCharge_kg=580.000000
    dbObj.fragCharge_kg=0.000000
    dbObj.radCharge_kg=58.000000
    dbObj.fragMetal_kg=0.000000
    dbObj.fragFragment_kg=0.000000
    dbObj.fragSpread=0.000000
    return dbObj
