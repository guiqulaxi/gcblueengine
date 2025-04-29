# -*- coding: utf-8 -*-
import pygcb
def CreateDBObject():
    dbObj=pygcb.tcWeaponDamage()
    dbObj.databaseClass='BlastFragAir120kg'
    dbObj.maxRange_m=4010.977295
    dbObj.probDetonate=0.850000
    dbObj.blastCharge_kg=21.831112
    dbObj.fragCharge_kg=55.045925
    dbObj.radCharge_kg=2.183111
    dbObj.fragMetal_kg=43.122963
    dbObj.fragFragment_kg=0.044138
    dbObj.fragSpread=0.300000
    return dbObj
