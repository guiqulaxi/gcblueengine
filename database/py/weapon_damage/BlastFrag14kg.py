# -*- coding: utf-8 -*-
import pygcb
def CreateDBObject():
    dbObj=pygcb.tcWeaponDamage()
    dbObj.databaseClass='BlastFrag14kg'
    dbObj.maxRange_m=677.823608
    dbObj.probDetonate=0.850000
    dbObj.blastCharge_kg=4.974913
    dbObj.fragCharge_kg=4.383391
    dbObj.radCharge_kg=0.497491
    dbObj.fragMetal_kg=4.641695
    dbObj.fragFragment_kg=0.001727
    dbObj.fragSpread=0.300000
    return dbObj
