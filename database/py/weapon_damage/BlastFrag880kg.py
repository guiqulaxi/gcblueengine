# -*- coding: utf-8 -*-
import pygcb
def CreateDBObject():
    dbObj=pygcb.tcWeaponDamage()
    dbObj.databaseClass='BlastFrag880kg'
    dbObj.maxRange_m=4336.513184
    dbObj.probDetonate=0.850000
    dbObj.blastCharge_kg=316.632782
    dbObj.fragCharge_kg=272.911469
    dbObj.radCharge_kg=31.663279
    dbObj.fragMetal_kg=290.455750
    dbObj.fragFragment_kg=0.055178
    dbObj.fragSpread=0.300000
    return dbObj
