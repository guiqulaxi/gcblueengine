# -*- coding: utf-8 -*-
import pygcb
def CreateDBObject():
    dbObj=pygcb.tcWeaponDamage()
    dbObj.databaseClass='BlastFrag25kg'
    dbObj.maxRange_m=894.203674
    dbObj.probDetonate=0.850000
    dbObj.blastCharge_kg=8.920612
    dbObj.fragCharge_kg=7.802925
    dbObj.radCharge_kg=0.892061
    dbObj.fragMetal_kg=8.276463
    dbObj.fragFragment_kg=0.002723
    dbObj.fragSpread=0.300000
    return dbObj
