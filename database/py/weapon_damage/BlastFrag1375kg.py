# -*- coding: utf-8 -*-
import pygcb
def CreateDBObject():
    dbObj=pygcb.tcWeaponDamage()
    dbObj.databaseClass='BlastFrag1375kg'
    dbObj.maxRange_m=5197.778809
    dbObj.probDetonate=0.850000
    dbObj.blastCharge_kg=494.821777
    dbObj.fragCharge_kg=426.368805
    dbObj.radCharge_kg=49.482178
    dbObj.fragMetal_kg=453.809418
    dbObj.fragFragment_kg=0.080807
    dbObj.fragSpread=0.300000
    return dbObj
