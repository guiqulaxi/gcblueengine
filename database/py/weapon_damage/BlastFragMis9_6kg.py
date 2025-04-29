# -*- coding: utf-8 -*-
import pygcb
def CreateDBObject():
    dbObj=pygcb.tcWeaponDamage()
    dbObj.databaseClass='BlastFragMis9.6kg'
    dbObj.maxRange_m=2299.295410
    dbObj.probDetonate=0.850000
    dbObj.blastCharge_kg=2.344493
    dbObj.fragCharge_kg=4.005004
    dbObj.radCharge_kg=0.234449
    dbObj.fragMetal_kg=3.250502
    dbObj.fragFragment_kg=0.014383
    dbObj.fragSpread=0.098526
    return dbObj
