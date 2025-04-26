# -*- coding: utf-8 -*-
import pygcb
def CreateDBObject():
    dbObj=pygcb.tcWeaponDamage()
    dbObj.databaseClass='BlastFragMis92.5kg'
    dbObj.maxRange_m=3838.120117
    dbObj.probDetonate=0.850000
    dbObj.blastCharge_kg=17.421940
    dbObj.fragCharge_kg=42.035374
    dbObj.radCharge_kg=1.742194
    dbObj.fragMetal_kg=33.042686
    dbObj.fragFragment_kg=0.040296
    dbObj.fragSpread=0.300000
    return dbObj
