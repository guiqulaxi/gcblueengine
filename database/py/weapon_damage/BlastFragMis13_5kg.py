# -*- coding: utf-8 -*-
import pygcb
def CreateDBObject():
    dbObj=pygcb.tcWeaponDamage()
    dbObj.databaseClass='BlastFragMis13.5kg'
    dbObj.maxRange_m=2566.886719
    dbObj.probDetonate=0.850000
    dbObj.blastCharge_kg=3.183432
    dbObj.fragCharge_kg=5.707712
    dbObj.radCharge_kg=0.318343
    dbObj.fragMetal_kg=4.608856
    dbObj.fragFragment_kg=0.017864
    dbObj.fragSpread=0.128403
    return dbObj
