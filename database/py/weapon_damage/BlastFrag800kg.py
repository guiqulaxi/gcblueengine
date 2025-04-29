# -*- coding: utf-8 -*-
import pygcb
def CreateDBObject():
    dbObj=pygcb.tcWeaponDamage()
    dbObj.databaseClass='BlastFrag800kg'
    dbObj.maxRange_m=4173.312500
    dbObj.probDetonate=0.850000
    dbObj.blastCharge_kg=287.835144
    dbObj.fragCharge_kg=248.109909
    dbObj.radCharge_kg=28.783514
    dbObj.fragMetal_kg=264.054962
    dbObj.fragFragment_kg=0.050937
    dbObj.fragSpread=0.300000
    return dbObj
