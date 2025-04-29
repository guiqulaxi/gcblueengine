# -*- coding: utf-8 -*-
import pygcb
def CreateDBObject():
    dbObj=pygcb.tcWeaponDamage()
    dbObj.databaseClass='BlastFragAir105kg'
    dbObj.maxRange_m=3902.652100
    dbObj.probDetonate=0.850000
    dbObj.blastCharge_kg=19.448017
    dbObj.fragCharge_kg=47.934654
    dbObj.radCharge_kg=1.944802
    dbObj.fragMetal_kg=37.617329
    dbObj.fragFragment_kg=0.041704
    dbObj.fragSpread=0.300000
    return dbObj
