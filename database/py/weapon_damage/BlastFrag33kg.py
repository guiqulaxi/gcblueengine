# -*- coding: utf-8 -*-
import pygcb
def CreateDBObject():
    dbObj=pygcb.tcWeaponDamage()
    dbObj.databaseClass='BlastFrag33kg'
    dbObj.maxRange_m=1011.660461
    dbObj.probDetonate=0.850000
    dbObj.blastCharge_kg=11.793765
    dbObj.fragCharge_kg=10.287490
    dbObj.radCharge_kg=1.179377
    dbObj.fragMetal_kg=10.918745
    dbObj.fragFragment_kg=0.003362
    dbObj.fragSpread=0.300000
    return dbObj
