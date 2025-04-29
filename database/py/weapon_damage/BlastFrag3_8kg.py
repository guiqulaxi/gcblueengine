# -*- coding: utf-8 -*-
import pygcb
def CreateDBObject():
    dbObj=pygcb.tcWeaponDamage()
    dbObj.databaseClass='BlastFrag3.8kg'
    dbObj.maxRange_m=346.337738
    dbObj.probDetonate=0.850000
    dbObj.blastCharge_kg=1.335075
    dbObj.fragCharge_kg=1.199950
    dbObj.radCharge_kg=0.133507
    dbObj.fragMetal_kg=1.264975
    dbObj.fragFragment_kg=0.000643
    dbObj.fragSpread=0.300000
    return dbObj
