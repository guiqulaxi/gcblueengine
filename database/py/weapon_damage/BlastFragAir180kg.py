# -*- coding: utf-8 -*-
import pygcb
def CreateDBObject():
    dbObj=pygcb.tcWeaponDamage()
    dbObj.databaseClass='BlastFragAir180kg'
    dbObj.maxRange_m=4304.593750
    dbObj.probDetonate=0.850000
    dbObj.blastCharge_kg=30.946667
    dbObj.fragCharge_kg=83.768890
    dbObj.radCharge_kg=3.094667
    dbObj.fragMetal_kg=65.284447
    dbObj.fragFragment_kg=0.051123
    dbObj.fragSpread=0.300000
    return dbObj
