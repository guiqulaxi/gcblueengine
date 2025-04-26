# -*- coding: utf-8 -*-
import pygcb
def CreateDBObject():
    dbObj=pygcb.tcWeaponDamage()
    dbObj.databaseClass='BlastFrag52.5kg'
    dbObj.maxRange_m=1254.365723
    dbObj.probDetonate=0.850000
    dbObj.blastCharge_kg=18.802315
    dbObj.fragCharge_kg=16.340124
    dbObj.radCharge_kg=1.880231
    dbObj.fragMetal_kg=17.357561
    dbObj.fragFragment_kg=0.004909
    dbObj.fragSpread=0.300000
    return dbObj
