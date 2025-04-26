# -*- coding: utf-8 -*-
import pygcb
def CreateDBObject():
    dbObj=pygcb.tcWeaponDamage()
    dbObj.databaseClass='BlastFragAir265kg'
    dbObj.maxRange_m=4582.318359
    dbObj.probDetonate=0.850000
    dbObj.blastCharge_kg=43.032536
    dbObj.fragCharge_kg=125.011642
    dbObj.radCharge_kg=4.303254
    dbObj.fragMetal_kg=96.955818
    dbObj.fragFragment_kg=0.058267
    dbObj.fragSpread=0.300000
    return dbObj
