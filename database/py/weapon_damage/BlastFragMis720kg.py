# -*- coding: utf-8 -*-
import pygcb
def CreateDBObject():
    dbObj=pygcb.tcWeaponDamage()
    dbObj.databaseClass='BlastFragMis720kg'
    dbObj.maxRange_m=6084.222656
    dbObj.probDetonate=0.850000
    dbObj.blastCharge_kg=99.169701
    dbObj.fragCharge_kg=351.486877
    dbObj.radCharge_kg=9.916970
    dbObj.fragMetal_kg=269.343445
    dbObj.fragFragment_kg=0.106586
    dbObj.fragSpread=0.300000
    return dbObj
