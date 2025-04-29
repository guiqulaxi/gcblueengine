# -*- coding: utf-8 -*-
import pygcb
def CreateDBObject():
    dbObj=pygcb.tcWeaponDamage()
    dbObj.databaseClass='BlastFrag2050kg'
    dbObj.maxRange_m=6059.970703
    dbObj.probDetonate=0.850000
    dbObj.blastCharge_kg=737.811951
    dbObj.fragCharge_kg=635.625366
    dbObj.radCharge_kg=73.781197
    dbObj.fragMetal_kg=676.562683
    dbObj.fragFragment_kg=0.112162
    dbObj.fragSpread=0.300000
    return dbObj
