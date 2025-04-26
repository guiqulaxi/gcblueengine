# -*- coding: utf-8 -*-
import pygcb
def CreateDBObject():
    dbObj=pygcb.tcWeaponDamage()
    dbObj.databaseClass='BlastFragMis13kg'
    dbObj.maxRange_m=2537.209717
    dbObj.probDetonate=0.850000
    dbObj.blastCharge_kg=3.077627
    dbObj.fragCharge_kg=5.488248
    dbObj.radCharge_kg=0.307763
    dbObj.fragMetal_kg=4.434124
    dbObj.fragFragment_kg=0.017457
    dbObj.fragSpread=0.124452
    return dbObj
