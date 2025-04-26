# -*- coding: utf-8 -*-
import pygcb
def CreateDBObject():
    dbObj=pygcb.tcWeaponDamage()
    dbObj.databaseClass='BlastFragMis200kg'
    dbObj.maxRange_m=4371.880859
    dbObj.probDetonate=0.850000
    dbObj.blastCharge_kg=33.865482
    dbObj.fragCharge_kg=93.423012
    dbObj.radCharge_kg=3.386548
    dbObj.fragMetal_kg=72.711502
    dbObj.fragFragment_kg=0.052804
    dbObj.fragSpread=0.300000
    return dbObj
