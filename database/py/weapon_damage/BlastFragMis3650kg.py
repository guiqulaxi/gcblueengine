# -*- coding: utf-8 -*-
import pygcb
def CreateDBObject():
    dbObj=pygcb.tcWeaponDamage()
    dbObj.databaseClass='BlastFragMis3650kg'
    dbObj.maxRange_m=11076.238281
    dbObj.probDetonate=0.850000
    dbObj.blastCharge_kg=356.611908
    dbObj.fragCharge_kg=1879.258789
    dbObj.radCharge_kg=35.661190
    dbObj.fragMetal_kg=1414.129395
    dbObj.fragFragment_kg=0.399584
    dbObj.fragSpread=0.300000
    return dbObj
