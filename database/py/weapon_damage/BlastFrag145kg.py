# -*- coding: utf-8 -*-
import pygcb
def CreateDBObject():
    dbObj=pygcb.tcWeaponDamage()
    dbObj.databaseClass='BlastFrag145kg'
    dbObj.maxRange_m=2030.822998
    dbObj.probDetonate=0.850000
    dbObj.blastCharge_kg=52.077259
    dbObj.fragCharge_kg=45.031826
    dbObj.radCharge_kg=5.207726
    dbObj.fragMetal_kg=47.890915
    dbObj.fragFragment_kg=0.012021
    dbObj.fragSpread=0.300000
    return dbObj
