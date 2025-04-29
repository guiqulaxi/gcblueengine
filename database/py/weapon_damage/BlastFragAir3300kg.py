# -*- coding: utf-8 -*-
import pygcb
def CreateDBObject():
    dbObj=pygcb.tcWeaponDamage()
    dbObj.databaseClass='BlastFragAir3300kg'
    dbObj.maxRange_m=10698.307617
    dbObj.probDetonate=0.850000
    dbObj.blastCharge_kg=330.620544
    dbObj.fragCharge_kg=1693.586304
    dbObj.radCharge_kg=33.062054
    dbObj.fragMetal_kg=1275.793213
    dbObj.fragFragment_kg=0.369581
    dbObj.fragSpread=0.300000
    return dbObj
