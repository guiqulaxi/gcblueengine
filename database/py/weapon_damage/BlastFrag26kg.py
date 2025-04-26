# -*- coding: utf-8 -*-
import pygcb
def CreateDBObject():
    dbObj=pygcb.tcWeaponDamage()
    dbObj.databaseClass='BlastFrag26kg'
    dbObj.maxRange_m=909.481934
    dbObj.probDetonate=0.850000
    dbObj.blastCharge_kg=9.279646
    dbObj.fragCharge_kg=8.113569
    dbObj.radCharge_kg=0.927965
    dbObj.fragMetal_kg=8.606785
    dbObj.fragFragment_kg=0.002802
    dbObj.fragSpread=0.300000
    return dbObj
