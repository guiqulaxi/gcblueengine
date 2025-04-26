# -*- coding: utf-8 -*-
import pygcb
def CreateDBObject():
    dbObj=pygcb.tcWeaponDamage()
    dbObj.databaseClass='BlastFrag97.5kg'
    dbObj.maxRange_m=1683.904053
    dbObj.probDetonate=0.850000
    dbObj.blastCharge_kg=34.987045
    dbObj.fragCharge_kg=30.300303
    dbObj.radCharge_kg=3.498705
    dbObj.fragMetal_kg=32.212650
    dbObj.fragFragment_kg=0.008424
    dbObj.fragSpread=0.300000
    return dbObj
