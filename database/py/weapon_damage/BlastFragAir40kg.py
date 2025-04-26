# -*- coding: utf-8 -*-
import pygcb
def CreateDBObject():
    dbObj=pygcb.tcWeaponDamage()
    dbObj.databaseClass='BlastFragAir40kg'
    dbObj.maxRange_m=3313.059814
    dbObj.probDetonate=0.850000
    dbObj.blastCharge_kg=8.360842
    dbObj.fragCharge_kg=17.626106
    dbObj.radCharge_kg=0.836084
    dbObj.fragMetal_kg=14.013053
    dbObj.fragFragment_kg=0.029815
    dbObj.fragSpread=0.300000
    return dbObj
