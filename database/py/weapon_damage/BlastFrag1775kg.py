# -*- coding: utf-8 -*-
import pygcb
def CreateDBObject():
    dbObj=pygcb.tcWeaponDamage()
    dbObj.databaseClass='BlastFrag1775kg'
    dbObj.maxRange_m=5737.927246
    dbObj.probDetonate=0.850000
    dbObj.blastCharge_kg=638.815491
    dbObj.fragCharge_kg=550.372986
    dbObj.radCharge_kg=63.881550
    dbObj.fragMetal_kg=585.811523
    dbObj.fragFragment_kg=0.099764
    dbObj.fragSpread=0.300000
    return dbObj
