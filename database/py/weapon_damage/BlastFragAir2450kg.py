# -*- coding: utf-8 -*-
import pygcb
def CreateDBObject():
    dbObj=pygcb.tcWeaponDamage()
    dbObj.databaseClass='BlastFragAir2450kg'
    dbObj.maxRange_m=9608.398438
    dbObj.probDetonate=0.850000
    dbObj.blastCharge_kg=263.457184
    dbObj.fragCharge_kg=1245.361938
    dbObj.radCharge_kg=26.345718
    dbObj.fragMetal_kg=941.180969
    dbObj.fragFragment_kg=0.290578
    dbObj.fragSpread=0.300000
    return dbObj
