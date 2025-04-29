# -*- coding: utf-8 -*-
import pygcb
def CreateDBObject():
    dbObj=pygcb.tcWeaponDamage()
    dbObj.databaseClass='BlastFrag3850kg'
    dbObj.maxRange_m=7767.753906
    dbObj.probDetonate=0.850000
    dbObj.blastCharge_kg=1385.796387
    dbObj.fragCharge_kg=1193.635742
    dbObj.radCharge_kg=138.579636
    dbObj.fragMetal_kg=1270.567871
    dbObj.fragFragment_kg=0.192277
    dbObj.fragSpread=0.300000
    return dbObj
