# -*- coding: utf-8 -*-
import pygcb
def CreateDBObject():
    dbObj=pygcb.tcWeaponDamage()
    dbObj.databaseClass='BlastFrag45kg'
    dbObj.maxRange_m=1168.479370
    dbObj.probDetonate=0.850000
    dbObj.blastCharge_kg=16.106115
    dbObj.fragCharge_kg=14.012589
    dbObj.radCharge_kg=1.610612
    dbObj.fragMetal_kg=14.881294
    dbObj.fragFragment_kg=0.004326
    dbObj.fragSpread=0.300000
    return dbObj
