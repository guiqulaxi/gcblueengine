# -*- coding: utf-8 -*-
import pygcb
def CreateDBObject():
    dbObj=pygcb.tcWeaponDamage()
    dbObj.databaseClass='BlastFragMis3.8kg'
    dbObj.maxRange_m=1575.738403
    dbObj.probDetonate=0.850000
    dbObj.blastCharge_kg=1.014884
    dbObj.fragCharge_kg=1.527411
    dbObj.radCharge_kg=0.101488
    dbObj.fragMetal_kg=1.257705
    dbObj.fragFragment_kg=0.006987
    dbObj.fragSpread=0.062500
    return dbObj
