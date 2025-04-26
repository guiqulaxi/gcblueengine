# -*- coding: utf-8 -*-
import pygcb
def CreateDBObject():
    dbObj=pygcb.tcWeaponDamage()
    dbObj.databaseClass='BlastFrag850kg'
    dbObj.maxRange_m=4277.537598
    dbObj.probDetonate=0.850000
    dbObj.blastCharge_kg=305.833649
    dbObj.fragCharge_kg=263.610901
    dbObj.radCharge_kg=30.583364
    dbObj.fragMetal_kg=280.555450
    dbObj.fragFragment_kg=0.053623
    dbObj.fragSpread=0.300000
    return dbObj
