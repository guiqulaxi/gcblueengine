# -*- coding: utf-8 -*-
import pygcb
def CreateDBObject():
    dbObj=pygcb.tcWeaponDamage()
    dbObj.databaseClass='BlastFrag41kg'
    dbObj.maxRange_m=1120.411133
    dbObj.probDetonate=0.850000
    dbObj.blastCharge_kg=14.668412
    dbObj.fragCharge_kg=12.771059
    dbObj.radCharge_kg=1.466841
    dbObj.fragMetal_kg=13.560530
    dbObj.fragFragment_kg=0.004017
    dbObj.fragSpread=0.300000
    return dbObj
