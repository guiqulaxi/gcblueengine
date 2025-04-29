# -*- coding: utf-8 -*-
import pygcb
def CreateDBObject():
    dbObj=pygcb.tcWeaponDamage()
    dbObj.databaseClass='BlastFrag1125kg'
    dbObj.maxRange_m=4792.432617
    dbObj.probDetonate=0.850000
    dbObj.blastCharge_kg=404.826721
    dbObj.fragCharge_kg=348.865509
    dbObj.radCharge_kg=40.482674
    dbObj.fragMetal_kg=371.307770
    dbObj.fragFragment_kg=0.068055
    dbObj.fragSpread=0.300000
    return dbObj
