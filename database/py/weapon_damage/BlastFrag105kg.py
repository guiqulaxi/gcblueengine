# -*- coding: utf-8 -*-
import pygcb
def CreateDBObject():
    dbObj=pygcb.tcWeaponDamage()
    dbObj.databaseClass='BlastFrag105kg'
    dbObj.maxRange_m=1743.846924
    dbObj.probDetonate=0.850000
    dbObj.blastCharge_kg=37.685219
    dbObj.fragCharge_kg=32.626522
    dbObj.radCharge_kg=3.768522
    dbObj.fragMetal_kg=34.688259
    dbObj.fragFragment_kg=0.008996
    dbObj.fragSpread=0.300000
    return dbObj
