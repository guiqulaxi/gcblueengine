# -*- coding: utf-8 -*-
import pygcb
def CreateDBObject():
    dbObj=pygcb.tcWeaponDamage()
    dbObj.databaseClass='BlastFragMis270kg'
    dbObj.maxRange_m=4607.052246
    dbObj.probDetonate=0.850000
    dbObj.blastCharge_kg=43.720001
    dbObj.fragCharge_kg=127.453331
    dbObj.radCharge_kg=4.372000
    dbObj.fragMetal_kg=98.826668
    dbObj.fragFragment_kg=0.058931
    dbObj.fragSpread=0.300000
    return dbObj
