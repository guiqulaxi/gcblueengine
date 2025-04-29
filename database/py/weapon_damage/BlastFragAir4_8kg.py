# -*- coding: utf-8 -*-
import pygcb
def CreateDBObject():
    dbObj=pygcb.tcWeaponDamage()
    dbObj.databaseClass='BlastFragAir4.8kg'
    dbObj.maxRange_m=1749.192505
    dbObj.probDetonate=0.850000
    dbObj.blastCharge_kg=1.254303
    dbObj.fragCharge_kg=1.947798
    dbObj.radCharge_kg=0.125430
    dbObj.fragMetal_kg=1.597899
    dbObj.fragFragment_kg=0.008499
    dbObj.fragSpread=0.068179
    return dbObj
