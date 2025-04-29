# -*- coding: utf-8 -*-
import pygcb
def CreateDBObject():
    dbObj=pygcb.tcWeaponDamage()
    dbObj.databaseClass='BlastFragAir65kg'
    dbObj.maxRange_m=3649.186768
    dbObj.probDetonate=0.850000
    dbObj.blastCharge_kg=12.808051
    dbObj.fragCharge_kg=29.161299
    dbObj.radCharge_kg=1.280805
    dbObj.fragMetal_kg=23.030649
    dbObj.fragFragment_kg=0.036326
    dbObj.fragSpread=0.300000
    return dbObj
