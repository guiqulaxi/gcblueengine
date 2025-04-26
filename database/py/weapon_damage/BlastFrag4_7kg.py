# -*- coding: utf-8 -*-
import pygcb
def CreateDBObject():
    dbObj=pygcb.tcWeaponDamage()
    dbObj.databaseClass='BlastFrag4.7kg'
    dbObj.maxRange_m=384.247986
    dbObj.probDetonate=0.850000
    dbObj.blastCharge_kg=1.653832
    dbObj.fragCharge_kg=1.482445
    dbObj.radCharge_kg=0.165383
    dbObj.fragMetal_kg=1.563722
    dbObj.fragFragment_kg=0.000740
    dbObj.fragSpread=0.300000
    return dbObj
