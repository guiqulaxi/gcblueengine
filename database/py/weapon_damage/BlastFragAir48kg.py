# -*- coding: utf-8 -*-
import pygcb
def CreateDBObject():
    dbObj=pygcb.tcWeaponDamage()
    dbObj.databaseClass='BlastFragAir48kg'
    dbObj.maxRange_m=3410.476074
    dbObj.probDetonate=0.850000
    dbObj.blastCharge_kg=9.817173
    dbObj.fragCharge_kg=21.295218
    dbObj.radCharge_kg=0.981717
    dbObj.fragMetal_kg=16.887609
    dbObj.fragFragment_kg=0.031625
    dbObj.fragSpread=0.300000
    return dbObj
