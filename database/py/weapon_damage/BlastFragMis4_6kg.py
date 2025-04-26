# -*- coding: utf-8 -*-
import pygcb
def CreateDBObject():
    dbObj=pygcb.tcWeaponDamage()
    dbObj.databaseClass='BlastFragMis4.6kg'
    dbObj.maxRange_m=1718.942749
    dbObj.probDetonate=0.850000
    dbObj.blastCharge_kg=1.206869
    dbObj.fragCharge_kg=1.863421
    dbObj.radCharge_kg=0.120687
    dbObj.fragMetal_kg=1.529710
    dbObj.fragFragment_kg=0.008224
    dbObj.fragSpread=0.066736
    return dbObj
