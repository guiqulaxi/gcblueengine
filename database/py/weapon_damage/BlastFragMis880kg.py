# -*- coding: utf-8 -*-
import pygcb
def CreateDBObject():
    dbObj=pygcb.tcWeaponDamage()
    dbObj.databaseClass='BlastFragMis880kg'
    dbObj.maxRange_m=6458.155762
    dbObj.probDetonate=0.850000
    dbObj.blastCharge_kg=116.852165
    dbObj.fragCharge_kg=432.498566
    dbObj.radCharge_kg=11.685217
    dbObj.fragMetal_kg=330.649292
    dbObj.fragFragment_kg=0.121250
    dbObj.fragSpread=0.300000
    return dbObj
