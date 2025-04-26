# -*- coding: utf-8 -*-
import pygcb
def CreateDBObject():
    dbObj=pygcb.tcWeaponDamage()
    dbObj.databaseClass='BlastFrag92.5kg'
    dbObj.maxRange_m=1644.594482
    dbObj.probDetonate=0.850000
    dbObj.blastCharge_kg=33.188347
    dbObj.fragCharge_kg=28.749437
    dbObj.radCharge_kg=3.318835
    dbObj.fragMetal_kg=30.562218
    dbObj.fragFragment_kg=0.008060
    dbObj.fragSpread=0.300000
    return dbObj
