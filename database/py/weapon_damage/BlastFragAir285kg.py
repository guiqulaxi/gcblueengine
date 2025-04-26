# -*- coding: utf-8 -*-
import pygcb
def CreateDBObject():
    dbObj=pygcb.tcWeaponDamage()
    dbObj.databaseClass='BlastFragAir285kg'
    dbObj.maxRange_m=4680.797363
    dbObj.probDetonate=0.850000
    dbObj.blastCharge_kg=45.768852
    dbObj.fragCharge_kg=134.787430
    dbObj.radCharge_kg=4.576885
    dbObj.fragMetal_kg=104.443718
    dbObj.fragFragment_kg=0.060936
    dbObj.fragSpread=0.300000
    return dbObj
