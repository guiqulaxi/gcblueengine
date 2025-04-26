# -*- coding: utf-8 -*-
import pygcb
def CreateDBObject():
    dbObj=pygcb.tcWeaponDamage()
    dbObj.databaseClass='BlastFrag34kg'
    dbObj.maxRange_m=1026.315186
    dbObj.probDetonate=0.850000
    dbObj.blastCharge_kg=12.153029
    dbObj.fragCharge_kg=10.597980
    dbObj.radCharge_kg=1.215303
    dbObj.fragMetal_kg=11.248990
    dbObj.fragFragment_kg=0.003446
    dbObj.fragSpread=0.300000
    return dbObj
