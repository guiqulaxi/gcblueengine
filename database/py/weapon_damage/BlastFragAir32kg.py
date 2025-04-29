# -*- coding: utf-8 -*-
import pygcb
def CreateDBObject():
    dbObj=pygcb.tcWeaponDamage()
    dbObj.databaseClass='BlastFragAir32kg'
    dbObj.maxRange_m=3181.739990
    dbObj.probDetonate=0.850000
    dbObj.blastCharge_kg=6.864782
    dbObj.fragCharge_kg=13.983479
    dbObj.radCharge_kg=0.686478
    dbObj.fragMetal_kg=11.151739
    dbObj.fragFragment_kg=0.027467
    dbObj.fragSpread=0.300000
    return dbObj
