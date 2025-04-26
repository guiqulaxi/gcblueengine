# -*- coding: utf-8 -*-
import pygcb
def CreateDBObject():
    dbObj=pygcb.tcWeaponDamage()
    dbObj.databaseClass='BlastFrag38kg'
    dbObj.maxRange_m=1081.780884
    dbObj.probDetonate=0.850000
    dbObj.blastCharge_kg=13.590286
    dbObj.fragCharge_kg=11.839809
    dbObj.radCharge_kg=1.359029
    dbObj.fragMetal_kg=12.569904
    dbObj.fragFragment_kg=0.003777
    dbObj.fragSpread=0.300000
    return dbObj
