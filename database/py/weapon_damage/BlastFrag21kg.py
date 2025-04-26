# -*- coding: utf-8 -*-
import pygcb
def CreateDBObject():
    dbObj=pygcb.tcWeaponDamage()
    dbObj.databaseClass='BlastFrag21kg'
    dbObj.maxRange_m=827.025574
    dbObj.probDetonate=0.850000
    dbObj.blastCharge_kg=7.484913
    dbObj.fragCharge_kg=6.560058
    dbObj.radCharge_kg=0.748491
    dbObj.fragMetal_kg=6.955029
    dbObj.fragFragment_kg=0.002388
    dbObj.fragSpread=0.300000
    return dbObj
