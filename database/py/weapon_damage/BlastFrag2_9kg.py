# -*- coding: utf-8 -*-
import pygcb
def CreateDBObject():
    dbObj=pygcb.tcWeaponDamage()
    dbObj.databaseClass='BlastFrag2.9kg'
    dbObj.maxRange_m=298.626984
    dbObj.probDetonate=0.850000
    dbObj.blastCharge_kg=1.017741
    dbObj.fragCharge_kg=0.916506
    dbObj.radCharge_kg=0.101774
    dbObj.fragMetal_kg=0.965753
    dbObj.fragFragment_kg=0.000529
    dbObj.fragSpread=0.300000
    return dbObj
