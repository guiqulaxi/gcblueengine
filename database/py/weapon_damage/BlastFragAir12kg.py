# -*- coding: utf-8 -*-
import pygcb
def CreateDBObject():
    dbObj=pygcb.tcWeaponDamage()
    dbObj.databaseClass='BlastFragAir12kg'
    dbObj.maxRange_m=2473.846191
    dbObj.probDetonate=0.850000
    dbObj.blastCharge_kg=2.864576
    dbObj.fragCharge_kg=5.050282
    dbObj.radCharge_kg=0.286458
    dbObj.fragMetal_kg=4.085141
    dbObj.fragFragment_kg=0.016606
    dbObj.fragSpread=0.116736
    return dbObj
