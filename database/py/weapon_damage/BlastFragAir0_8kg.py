# -*- coding: utf-8 -*-
import pygcb
def CreateDBObject():
    dbObj=pygcb.tcWeaponDamage()
    dbObj.databaseClass='BlastFragAir0.8kg'
    dbObj.maxRange_m=685.793640
    dbObj.probDetonate=0.850000
    dbObj.blastCharge_kg=0.240000
    dbObj.fragCharge_kg=0.304000
    dbObj.radCharge_kg=0.024000
    dbObj.fragMetal_kg=0.256000
    dbObj.fragFragment_kg=0.001641
    dbObj.fragSpread=0.046944
    return dbObj
