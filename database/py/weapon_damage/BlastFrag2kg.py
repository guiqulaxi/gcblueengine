# -*- coding: utf-8 -*-
import pygcb
def CreateDBObject():
    dbObj=pygcb.tcWeaponDamage()
    dbObj.databaseClass='BlastFrag2kg'
    dbObj.maxRange_m=235.694046
    dbObj.probDetonate=0.850000
    dbObj.blastCharge_kg=0.702905
    dbObj.fragCharge_kg=0.631397
    dbObj.radCharge_kg=0.070290
    dbObj.fragMetal_kg=0.665698
    dbObj.fragFragment_kg=0.000396
    dbObj.fragSpread=0.300000
    return dbObj
