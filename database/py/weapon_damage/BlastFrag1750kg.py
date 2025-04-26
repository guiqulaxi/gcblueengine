# -*- coding: utf-8 -*-
import pygcb
def CreateDBObject():
    dbObj=pygcb.tcWeaponDamage()
    dbObj.databaseClass='BlastFrag1750kg'
    dbObj.maxRange_m=5707.295410
    dbObj.probDetonate=0.850000
    dbObj.blastCharge_kg=629.815857
    dbObj.fragCharge_kg=542.622803
    dbObj.radCharge_kg=62.981583
    dbObj.fragMetal_kg=577.561401
    dbObj.fragFragment_kg=0.098627
    dbObj.fragSpread=0.300000
    return dbObj
