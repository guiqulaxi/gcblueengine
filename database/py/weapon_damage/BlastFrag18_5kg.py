# -*- coding: utf-8 -*-
import pygcb
def CreateDBObject():
    dbObj=pygcb.tcWeaponDamage()
    dbObj.databaseClass='BlastFrag18.5kg'
    dbObj.maxRange_m=779.170837
    dbObj.probDetonate=0.850000
    dbObj.blastCharge_kg=6.588039
    dbObj.fragCharge_kg=5.782974
    dbObj.radCharge_kg=0.658804
    dbObj.fragMetal_kg=6.128987
    dbObj.fragFragment_kg=0.002164
    dbObj.fragSpread=0.300000
    return dbObj
