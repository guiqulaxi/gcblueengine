# -*- coding: utf-8 -*-
import pygcb
def CreateDBObject():
    dbObj=pygcb.tcWeaponDamage()
    dbObj.databaseClass='BlastFrag1725kg'
    dbObj.maxRange_m=5676.291504
    dbObj.probDetonate=0.850000
    dbObj.blastCharge_kg=620.816162
    dbObj.fragCharge_kg=534.872559
    dbObj.radCharge_kg=62.081619
    dbObj.fragMetal_kg=569.311279
    dbObj.fragFragment_kg=0.097485
    dbObj.fragSpread=0.300000
    return dbObj
