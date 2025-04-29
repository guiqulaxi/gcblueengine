# -*- coding: utf-8 -*-
import pygcb
def CreateDBObject():
    dbObj=pygcb.tcWeaponDamage()
    dbObj.databaseClass='BlastFragAir1825kg'
    dbObj.maxRange_m=8580.339844
    dbObj.probDetonate=0.850000
    dbObj.blastCharge_kg=209.504532
    dbObj.fragCharge_kg=918.830322
    dbObj.radCharge_kg=20.950453
    dbObj.fragMetal_kg=696.665161
    dbObj.fragFragment_kg=0.225970
    dbObj.fragSpread=0.300000
    return dbObj
