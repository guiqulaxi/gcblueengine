# -*- coding: utf-8 -*-
import pygcb
def CreateDBObject():
    dbObj=pygcb.tcWeaponDamage()
    dbObj.databaseClass='BlastFragMis1.5kg'
    dbObj.maxRange_m=982.906799
    dbObj.probDetonate=0.850000
    dbObj.blastCharge_kg=0.435000
    dbObj.fragCharge_kg=0.580000
    dbObj.radCharge_kg=0.043500
    dbObj.fragMetal_kg=0.485000
    dbObj.fragFragment_kg=0.002994
    dbObj.fragSpread=0.050625
    return dbObj
