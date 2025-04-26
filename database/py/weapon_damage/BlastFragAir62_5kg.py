# -*- coding: utf-8 -*-
import pygcb
def CreateDBObject():
    dbObj=pygcb.tcWeaponDamage()
    dbObj.databaseClass='BlastFragAir62.5kg'
    dbObj.maxRange_m=3617.707275
    dbObj.probDetonate=0.850000
    dbObj.blastCharge_kg=12.375890
    dbObj.fragCharge_kg=27.999407
    dbObj.radCharge_kg=1.237589
    dbObj.fragMetal_kg=22.124702
    dbObj.fragFragment_kg=0.035685
    dbObj.fragSpread=0.300000
    return dbObj
