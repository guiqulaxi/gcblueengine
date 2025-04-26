# -*- coding: utf-8 -*-
import pygcb
def CreateDBObject():
    dbObj=pygcb.tcWeaponDamage()
    dbObj.databaseClass='BlastFragAir1200kg'
    dbObj.maxRange_m=7231.262695
    dbObj.probDetonate=0.850000
    dbObj.blastCharge_kg=150.164627
    dbObj.fragCharge_kg=595.890259
    dbObj.radCharge_kg=15.016462
    dbObj.fragMetal_kg=453.945129
    dbObj.fragFragment_kg=0.155089
    dbObj.fragSpread=0.300000
    return dbObj
