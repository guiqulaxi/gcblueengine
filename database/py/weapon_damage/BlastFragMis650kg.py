# -*- coding: utf-8 -*-
import pygcb
def CreateDBObject():
    dbObj=pygcb.tcWeaponDamage()
    dbObj.databaseClass='BlastFragMis650kg'
    dbObj.maxRange_m=5892.145020
    dbObj.probDetonate=0.850000
    dbObj.blastCharge_kg=91.167831
    dbObj.fragCharge_kg=316.221436
    dbObj.radCharge_kg=9.116783
    dbObj.fragMetal_kg=242.610718
    dbObj.fragFragment_kg=0.099471
    dbObj.fragSpread=0.300000
    return dbObj
