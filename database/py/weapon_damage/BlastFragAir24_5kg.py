# -*- coding: utf-8 -*-
import pygcb
def CreateDBObject():
    dbObj=pygcb.tcWeaponDamage()
    dbObj.databaseClass='BlastFragAir24.5kg'
    dbObj.maxRange_m=3007.878662
    dbObj.probDetonate=0.850000
    dbObj.blastCharge_kg=5.417220
    dbObj.fragCharge_kg=10.598520
    dbObj.radCharge_kg=0.541722
    dbObj.fragMetal_kg=8.484260
    dbObj.fragFragment_kg=0.024521
    dbObj.fragSpread=0.230934
    return dbObj
