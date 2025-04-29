# -*- coding: utf-8 -*-
import pygcb
def CreateDBObject():
    dbObj=pygcb.tcWeaponDamage()
    dbObj.databaseClass='BlastFrag62.5kg'
    dbObj.maxRange_m=1367.750977
    dbObj.probDetonate=0.850000
    dbObj.blastCharge_kg=22.398014
    dbObj.fragCharge_kg=19.442991
    dbObj.radCharge_kg=2.239801
    dbObj.fragMetal_kg=20.658995
    dbObj.fragFragment_kg=0.005739
    dbObj.fragSpread=0.300000
    return dbObj
