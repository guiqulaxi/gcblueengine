# -*- coding: utf-8 -*-
import pygcb
def CreateDBObject():
    dbObj=pygcb.tcWeaponDamage()
    dbObj.databaseClass='BlastFragAir38kg'
    dbObj.maxRange_m=3284.042480
    dbObj.probDetonate=0.850000
    dbObj.blastCharge_kg=7.990871
    dbObj.fragCharge_kg=16.712753
    dbObj.radCharge_kg=0.799087
    dbObj.fragMetal_kg=13.296376
    dbObj.fragFragment_kg=0.029287
    dbObj.fragSpread=0.300000
    return dbObj
