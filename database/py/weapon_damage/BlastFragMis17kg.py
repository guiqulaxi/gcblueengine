# -*- coding: utf-8 -*-
import pygcb
def CreateDBObject():
    dbObj=pygcb.tcWeaponDamage()
    dbObj.databaseClass='BlastFragMis17kg'
    dbObj.maxRange_m=2744.489990
    dbObj.probDetonate=0.850000
    dbObj.blastCharge_kg=3.912114
    dbObj.fragCharge_kg=7.251924
    dbObj.radCharge_kg=0.391211
    dbObj.fragMetal_kg=5.835962
    dbObj.fragFragment_kg=0.020405
    dbObj.fragSpread=0.157785
    return dbObj
