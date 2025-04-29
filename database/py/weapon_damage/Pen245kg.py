# -*- coding: utf-8 -*-
import pygcb
def CreateDBObject():
    dbObj=pygcb.tcWeaponDamage()
    dbObj.databaseClass='Pen245kg'
    dbObj.maxRange_m=69.393860
    dbObj.probDetonate=0.850000
    dbObj.blastCharge_kg=171.500000
    dbObj.fragCharge_kg=0.000000
    dbObj.radCharge_kg=24.500000
    dbObj.fragMetal_kg=0.000000
    dbObj.fragFragment_kg=0.000000
    dbObj.fragSpread=0.000000
    return dbObj
