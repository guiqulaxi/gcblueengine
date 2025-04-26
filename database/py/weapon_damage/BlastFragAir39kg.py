# -*- coding: utf-8 -*-
import pygcb
def CreateDBObject():
    dbObj=pygcb.tcWeaponDamage()
    dbObj.databaseClass='BlastFragAir39kg'
    dbObj.maxRange_m=3298.825195
    dbObj.probDetonate=0.850000
    dbObj.blastCharge_kg=8.176172
    dbObj.fragCharge_kg=17.169218
    dbObj.radCharge_kg=0.817617
    dbObj.fragMetal_kg=13.654609
    dbObj.fragFragment_kg=0.029555
    dbObj.fragSpread=0.300000
    return dbObj
