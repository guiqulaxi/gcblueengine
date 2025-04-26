# -*- coding: utf-8 -*-
import pygcb
def CreateDBObject():
    dbObj=pygcb.tcWeaponDamage()
    dbObj.databaseClass='BlastFragMis365kg'
    dbObj.maxRange_m=5007.357910
    dbObj.probDetonate=0.850000
    dbObj.blastCharge_kg=56.389080
    dbObj.fragCharge_kg=174.107285
    dbObj.radCharge_kg=5.638908
    dbObj.fragMetal_kg=134.503647
    dbObj.fragFragment_kg=0.070274
    dbObj.fragSpread=0.300000
    return dbObj
