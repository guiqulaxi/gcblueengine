# -*- coding: utf-8 -*-
import pygcb
def CreateDBObject():
    dbObj=pygcb.tcWeaponDamage()
    dbObj.databaseClass='BlastFragAir150kg'
    dbObj.maxRange_m=4179.324707
    dbObj.probDetonate=0.850000
    dbObj.blastCharge_kg=26.463379
    dbObj.fragCharge_kg=69.357750
    dbObj.radCharge_kg=2.646338
    dbObj.fragMetal_kg=54.178875
    dbObj.fragFragment_kg=0.048074
    dbObj.fragSpread=0.300000
    return dbObj
