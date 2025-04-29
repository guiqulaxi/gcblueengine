# -*- coding: utf-8 -*-
import pygcb
def CreateDBObject():
    dbObj=pygcb.tcWeaponDamage()
    dbObj.databaseClass='BlastFrag2.1kg'
    dbObj.maxRange_m=243.715591
    dbObj.probDetonate=0.850000
    dbObj.blastCharge_kg=0.737702
    dbObj.fragCharge_kg=0.663199
    dbObj.radCharge_kg=0.073770
    dbObj.fragMetal_kg=0.699099
    dbObj.fragFragment_kg=0.000412
    dbObj.fragSpread=0.300000
    return dbObj
