# -*- coding: utf-8 -*-
import pygcb
def CreateDBObject():
    dbObj=pygcb.tcWeaponDamage()
    dbObj.databaseClass='BlastFragAir580kg'
    dbObj.maxRange_m=5676.355957
    dbObj.probDetonate=0.850000
    dbObj.blastCharge_kg=82.979683
    dbObj.fragCharge_kg=281.080200
    dbObj.radCharge_kg=8.297968
    dbObj.fragMetal_kg=215.940109
    dbObj.fragFragment_kg=0.091811
    dbObj.fragSpread=0.300000
    return dbObj
