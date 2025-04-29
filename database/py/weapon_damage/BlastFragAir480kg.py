# -*- coding: utf-8 -*-
import pygcb
def CreateDBObject():
    dbObj=pygcb.tcWeaponDamage()
    dbObj.databaseClass='BlastFragAir480kg'
    dbObj.maxRange_m=5347.807129
    dbObj.probDetonate=0.850000
    dbObj.blastCharge_kg=70.913139
    dbObj.fragCharge_kg=231.124573
    dbObj.radCharge_kg=7.091313
    dbObj.fragMetal_kg=177.962296
    dbObj.fragFragment_kg=0.080818
    dbObj.fragSpread=0.300000
    return dbObj
