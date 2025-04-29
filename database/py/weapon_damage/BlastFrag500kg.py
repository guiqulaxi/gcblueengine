# -*- coding: utf-8 -*-
import pygcb
def CreateDBObject():
    dbObj=pygcb.tcWeaponDamage()
    dbObj.databaseClass='BlastFrag500kg'
    dbObj.maxRange_m=3415.967041
    dbObj.probDetonate=0.850000
    dbObj.blastCharge_kg=179.846725
    dbObj.fragCharge_kg=155.102188
    dbObj.radCharge_kg=17.984673
    dbObj.fragMetal_kg=165.051086
    dbObj.fragFragment_kg=0.033711
    dbObj.fragSpread=0.300000
    return dbObj
