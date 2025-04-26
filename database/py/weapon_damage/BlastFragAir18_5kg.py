# -*- coding: utf-8 -*-
import pygcb
def CreateDBObject():
    dbObj=pygcb.tcWeaponDamage()
    dbObj.databaseClass='BlastFragAir18.5kg'
    dbObj.maxRange_m=2807.680176
    dbObj.probDetonate=0.850000
    dbObj.blastCharge_kg=4.218720
    dbObj.fragCharge_kg=7.917520
    dbObj.radCharge_kg=0.421872
    dbObj.fragMetal_kg=6.363760
    dbObj.fragFragment_kg=0.021355
    dbObj.fragSpread=0.171304
    return dbObj
