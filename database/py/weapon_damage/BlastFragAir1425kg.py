# -*- coding: utf-8 -*-
import pygcb
def CreateDBObject():
    dbObj=pygcb.tcWeaponDamage()
    dbObj.databaseClass='BlastFragAir1425kg'
    dbObj.maxRange_m=7766.715332
    dbObj.probDetonate=0.850000
    dbObj.blastCharge_kg=172.280853
    dbObj.fragCharge_kg=711.646118
    dbObj.radCharge_kg=17.228085
    dbObj.fragMetal_kg=541.073059
    dbObj.fragFragment_kg=0.181386
    dbObj.fragSpread=0.300000
    return dbObj
