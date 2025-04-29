# -*- coding: utf-8 -*-
import pygcb
def CreateDBObject():
    dbObj=pygcb.tcWeaponDamage()
    dbObj.databaseClass='BlastFragMis660kg'
    dbObj.maxRange_m=5920.390625
    dbObj.probDetonate=0.850000
    dbObj.blastCharge_kg=92.321899
    dbObj.fragCharge_kg=321.252075
    dbObj.radCharge_kg=9.232190
    dbObj.fragMetal_kg=246.426041
    dbObj.fragFragment_kg=0.100500
    dbObj.fragSpread=0.300000
    return dbObj
