# -*- coding: utf-8 -*-
import pygcb
def CreateDBObject():
    dbObj=pygcb.tcWeaponDamage()
    dbObj.databaseClass='BlastFragAir2.9kg'
    dbObj.maxRange_m=1385.503540
    dbObj.probDetonate=0.850000
    dbObj.blastCharge_kg=0.793849
    dbObj.fragCharge_kg=1.152767
    dbObj.radCharge_kg=0.079385
    dbObj.fragMetal_kg=0.953384
    dbObj.fragFragment_kg=0.005511
    dbObj.fragSpread=0.057733
    return dbObj
