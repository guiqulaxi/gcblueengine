# -*- coding: utf-8 -*-
import pygcb
def CreateDBObject():
    dbObj=pygcb.tcWeaponDamage()
    dbObj.databaseClass='BlastFragAir1850kg'
    dbObj.maxRange_m=8626.791016
    dbObj.probDetonate=0.850000
    dbObj.blastCharge_kg=211.753677
    dbObj.fragCharge_kg=931.830872
    dbObj.radCharge_kg=21.175367
    dbObj.fragMetal_kg=706.415466
    dbObj.fragFragment_kg=0.228687
    dbObj.fragSpread=0.300000
    return dbObj
