# -*- coding: utf-8 -*-
import pygcb
def CreateDBObject():
    dbObj=pygcb.tcWeaponDamage()
    dbObj.databaseClass='BlastFragMis395kg'
    dbObj.maxRange_m=5108.221680
    dbObj.probDetonate=0.850000
    dbObj.blastCharge_kg=60.254299
    dbObj.fragCharge_kg=188.930466
    dbObj.radCharge_kg=6.025430
    dbObj.fragMetal_kg=145.815231
    dbObj.fragFragment_kg=0.073311
    dbObj.fragSpread=0.300000
    return dbObj
