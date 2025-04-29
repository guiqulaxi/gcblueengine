# -*- coding: utf-8 -*-
import pygcb
def CreateDBObject():
    dbObj=pygcb.tcWeaponDamage()
    dbObj.databaseClass='BlastFrag355kg'
    dbObj.maxRange_m=2957.142334
    dbObj.probDetonate=0.850000
    dbObj.blastCharge_kg=127.655174
    dbObj.fragCharge_kg=110.146553
    dbObj.radCharge_kg=12.765517
    dbObj.fragMetal_kg=117.198273
    dbObj.fragFragment_kg=0.025171
    dbObj.fragSpread=0.300000
    return dbObj
