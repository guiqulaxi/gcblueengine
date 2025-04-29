# -*- coding: utf-8 -*-
import pygcb
def CreateDBObject():
    dbObj=pygcb.tcWeaponDamage()
    dbObj.databaseClass='BlastFragAir2.2kg'
    dbObj.maxRange_m=1207.954224
    dbObj.probDetonate=0.850000
    dbObj.blastCharge_kg=0.617219
    dbObj.fragCharge_kg=0.864520
    dbObj.radCharge_kg=0.061722
    dbObj.fragMetal_kg=0.718260
    dbObj.fragFragment_kg=0.004301
    dbObj.fragSpread=0.053798
    return dbObj
