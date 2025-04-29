# -*- coding: utf-8 -*-
import pygcb
def CreateDBObject():
    dbObj=pygcb.tcWeaponDamage()
    dbObj.databaseClass='BlastFragAir2kg'
    dbObj.maxRange_m=1147.318726
    dbObj.probDetonate=0.850000
    dbObj.blastCharge_kg=0.565810
    dbObj.fragCharge_kg=0.782793
    dbObj.radCharge_kg=0.056581
    dbObj.fragMetal_kg=0.651397
    dbObj.fragFragment_kg=0.003924
    dbObj.fragSpread=0.053156
    return dbObj
