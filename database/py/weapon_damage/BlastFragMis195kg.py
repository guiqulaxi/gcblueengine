# -*- coding: utf-8 -*-
import pygcb
def CreateDBObject():
    dbObj=pygcb.tcWeaponDamage()
    dbObj.databaseClass='BlastFragMis195kg'
    dbObj.maxRange_m=4356.052246
    dbObj.probDetonate=0.850000
    dbObj.blastCharge_kg=33.140606
    dbObj.fragCharge_kg=91.006264
    dbObj.radCharge_kg=3.314061
    dbObj.fragMetal_kg=70.853134
    dbObj.fragFragment_kg=0.052406
    dbObj.fragSpread=0.300000
    return dbObj
