# -*- coding: utf-8 -*-
import pygcb
def CreateDBObject():
    dbObj=pygcb.tcWeaponDamage()
    dbObj.databaseClass='BlastFragMis3150kg'
    dbObj.maxRange_m=10526.038086
    dbObj.probDetonate=0.850000
    dbObj.blastCharge_kg=319.206390
    dbObj.fragCharge_kg=1614.195679
    dbObj.radCharge_kg=31.920641
    dbObj.fragMetal_kg=1216.597900
    dbObj.fragFragment_kg=0.356356
    dbObj.fragSpread=0.300000
    return dbObj
