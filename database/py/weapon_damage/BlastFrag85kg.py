# -*- coding: utf-8 -*-
import pygcb
def CreateDBObject():
    dbObj=pygcb.tcWeaponDamage()
    dbObj.databaseClass='BlastFrag85kg'
    dbObj.maxRange_m=1582.458008
    dbObj.probDetonate=0.850000
    dbObj.blastCharge_kg=30.490431
    dbObj.fragCharge_kg=26.423046
    dbObj.radCharge_kg=3.049043
    dbObj.fragMetal_kg=28.086523
    dbObj.fragFragment_kg=0.007502
    dbObj.fragSpread=0.300000
    return dbObj
