# -*- coding: utf-8 -*-
import pygcb
def CreateDBObject():
    dbObj=pygcb.tcWeaponDamage()
    dbObj.databaseClass='BlastFragAir29kg'
    dbObj.maxRange_m=3119.693359
    dbObj.probDetonate=0.850000
    dbObj.blastCharge_kg=6.291615
    dbObj.fragCharge_kg=12.625589
    dbObj.radCharge_kg=0.629162
    dbObj.fragMetal_kg=10.082795
    dbObj.fragFragment_kg=0.026395
    dbObj.fragSpread=0.281489
    return dbObj
