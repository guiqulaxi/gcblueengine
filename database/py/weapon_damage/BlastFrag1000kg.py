# -*- coding: utf-8 -*-
import pygcb
def CreateDBObject():
    dbObj=pygcb.tcWeaponDamage()
    dbObj.databaseClass='BlastFrag1000kg'
    dbObj.maxRange_m=4563.385254
    dbObj.probDetonate=0.850000
    dbObj.blastCharge_kg=359.829620
    dbObj.fragCharge_kg=310.113586
    dbObj.radCharge_kg=35.982964
    dbObj.fragMetal_kg=330.056793
    dbObj.fragFragment_kg=0.061394
    dbObj.fragSpread=0.300000
    return dbObj
