# -*- coding: utf-8 -*-
import pygcb
def CreateDBObject():
    dbObj=pygcb.tcWeaponDamage()
    dbObj.databaseClass='BlastFrag720kg'
    dbObj.maxRange_m=3996.740234
    dbObj.probDetonate=0.850000
    dbObj.blastCharge_kg=259.037750
    dbObj.fragCharge_kg=223.308182
    dbObj.radCharge_kg=25.903774
    dbObj.fragMetal_kg=237.654083
    dbObj.fragFragment_kg=0.046562
    dbObj.fragSpread=0.300000
    return dbObj
