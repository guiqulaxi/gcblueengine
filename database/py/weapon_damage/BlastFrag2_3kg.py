# -*- coding: utf-8 -*-
import pygcb
def CreateDBObject():
    dbObj=pygcb.tcWeaponDamage()
    dbObj.databaseClass='BlastFrag2.3kg'
    dbObj.maxRange_m=258.885925
    dbObj.probDetonate=0.850000
    dbObj.blastCharge_kg=0.807458
    dbObj.fragCharge_kg=0.726695
    dbObj.radCharge_kg=0.080746
    dbObj.fragMetal_kg=0.765847
    dbObj.fragFragment_kg=0.000443
    dbObj.fragSpread=0.300000
    return dbObj
