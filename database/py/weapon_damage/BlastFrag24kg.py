# -*- coding: utf-8 -*-
import pygcb
def CreateDBObject():
    dbObj=pygcb.tcWeaponDamage()
    dbObj.databaseClass='BlastFrag24kg'
    dbObj.maxRange_m=878.358704
    dbObj.probDetonate=0.850000
    dbObj.blastCharge_kg=8.561620
    dbObj.fragCharge_kg=7.492254
    dbObj.radCharge_kg=0.856162
    dbObj.fragMetal_kg=7.946127
    dbObj.fragFragment_kg=0.002642
    dbObj.fragSpread=0.300000
    return dbObj
