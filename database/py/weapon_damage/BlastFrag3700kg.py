# -*- coding: utf-8 -*-
import pygcb
def CreateDBObject():
    dbObj=pygcb.tcWeaponDamage()
    dbObj.databaseClass='BlastFrag3700kg'
    dbObj.maxRange_m=7653.520020
    dbObj.probDetonate=0.850000
    dbObj.blastCharge_kg=1331.797363
    dbObj.fragCharge_kg=1147.135132
    dbObj.radCharge_kg=133.179733
    dbObj.fragMetal_kg=1221.067505
    dbObj.fragFragment_kg=0.186138
    dbObj.fragSpread=0.300000
    return dbObj
