# -*- coding: utf-8 -*-
import pygcb
def CreateDBObject():
    dbObj=pygcb.tcWeaponDamage()
    dbObj.databaseClass='BlastFragAir2550kg'
    dbObj.maxRange_m=9752.291016
    dbObj.probDetonate=0.850000
    dbObj.blastCharge_kg=271.694580
    dbObj.fragCharge_kg=1297.870239
    dbObj.radCharge_kg=27.169456
    dbObj.fragMetal_kg=980.435120
    dbObj.fragFragment_kg=0.300378
    dbObj.fragSpread=0.300000
    return dbObj
