# -*- coding: utf-8 -*-
import pygcb
def CreateDBObject():
    dbObj=pygcb.tcWeaponDamage()
    dbObj.databaseClass='BlastFrag0.1kg'
    dbObj.maxRange_m=82.005951
    dbObj.probDetonate=0.850000
    dbObj.blastCharge_kg=0.036000
    dbObj.fragCharge_kg=0.031000
    dbObj.radCharge_kg=0.003600
    dbObj.fragMetal_kg=0.033000
    dbObj.fragFragment_kg=0.000147
    dbObj.fragSpread=0.300000
    return dbObj
