# -*- coding: utf-8 -*-
import pygcb
def CreateDBObject():
    dbObj=pygcb.tcWeaponDamage()
    dbObj.databaseClass='BlastFragMis130kg'
    dbObj.maxRange_m=4073.230225
    dbObj.probDetonate=0.850000
    dbObj.blastCharge_kg=23.393738
    dbObj.fragCharge_kg=59.804176
    dbObj.radCharge_kg=2.339374
    dbObj.fragMetal_kg=46.802086
    dbObj.fragFragment_kg=0.045572
    dbObj.fragSpread=0.300000
    return dbObj
