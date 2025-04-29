# -*- coding: utf-8 -*-
import pygcb
def CreateDBObject():
    dbObj=pygcb.tcWeaponDamage()
    dbObj.databaseClass='BlastFragAir1100kg'
    dbObj.maxRange_m=6970.124512
    dbObj.probDetonate=0.850000
    dbObj.blastCharge_kg=140.011475
    dbObj.fragCharge_kg=544.658997
    dbObj.radCharge_kg=14.001147
    dbObj.fragMetal_kg=415.329498
    dbObj.fragFragment_kg=0.143118
    dbObj.fragSpread=0.300000
    return dbObj
