# -*- coding: utf-8 -*-
import pygcb
def CreateDBObject():
    dbObj=pygcb.tcWeaponDamage()
    dbObj.databaseClass='BlastFragMis940kg'
    dbObj.maxRange_m=6579.260742
    dbObj.probDetonate=0.850000
    dbObj.blastCharge_kg=123.290237
    dbObj.fragCharge_kg=463.006500
    dbObj.radCharge_kg=12.329023
    dbObj.fragMetal_kg=353.703247
    dbObj.fragFragment_kg=0.126232
    dbObj.fragSpread=0.300000
    return dbObj
