# -*- coding: utf-8 -*-
import pygcb
def CreateDBObject():
    dbObj=pygcb.tcWeaponDamage()
    dbObj.databaseClass='BlastFragMis420kg'
    dbObj.maxRange_m=5184.650879
    dbObj.probDetonate=0.850000
    dbObj.blastCharge_kg=63.432175
    dbObj.fragCharge_kg=201.311890
    dbObj.radCharge_kg=6.343217
    dbObj.fragMetal_kg=155.255936
    dbObj.fragFragment_kg=0.075661
    dbObj.fragSpread=0.300000
    return dbObj
