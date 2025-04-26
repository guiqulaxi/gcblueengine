# -*- coding: utf-8 -*-
import pygcb
def CreateDBObject():
    dbObj=pygcb.tcWeaponDamage()
    dbObj.databaseClass='BlastFragMis260kg'
    dbObj.maxRange_m=4555.742188
    dbObj.probDetonate=0.850000
    dbObj.blastCharge_kg=42.342747
    dbObj.fragCharge_kg=122.571503
    dbObj.radCharge_kg=4.234275
    dbObj.fragMetal_kg=95.085754
    dbObj.fragFragment_kg=0.057558
    dbObj.fragSpread=0.300000
    return dbObj
