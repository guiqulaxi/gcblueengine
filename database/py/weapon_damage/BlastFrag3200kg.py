# -*- coding: utf-8 -*-
import pygcb
def CreateDBObject():
    dbObj=pygcb.tcWeaponDamage()
    dbObj.databaseClass='BlastFrag3200kg'
    dbObj.maxRange_m=7242.835449
    dbObj.probDetonate=0.850000
    dbObj.blastCharge_kg=1151.800903
    dbObj.fragCharge_kg=992.132690
    dbObj.radCharge_kg=115.180092
    dbObj.fragMetal_kg=1056.066406
    dbObj.fragFragment_kg=0.165010
    dbObj.fragSpread=0.300000
    return dbObj
