# -*- coding: utf-8 -*-
import pygcb
def CreateDBObject():
    dbObj=pygcb.tcWeaponDamage()
    dbObj.databaseClass='BlastFragMis16kg'
    dbObj.maxRange_m=2698.480713
    dbObj.probDetonate=0.850000
    dbObj.blastCharge_kg=3.705913
    dbObj.fragCharge_kg=6.809391
    dbObj.radCharge_kg=0.370591
    dbObj.fragMetal_kg=5.484696
    dbObj.fragFragment_kg=0.019729
    dbObj.fragSpread=0.149082
    return dbObj
