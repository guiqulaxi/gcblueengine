# -*- coding: utf-8 -*-
import pygcb
def CreateDBObject():
    dbObj=pygcb.tcWeaponDamage()
    dbObj.databaseClass='BlastFrag960kg'
    dbObj.maxRange_m=4488.177734
    dbObj.probDetonate=0.850000
    dbObj.blastCharge_kg=345.430634
    dbObj.fragCharge_kg=297.712921
    dbObj.radCharge_kg=34.543064
    dbObj.fragMetal_kg=316.856445
    dbObj.fragFragment_kg=0.059292
    dbObj.fragSpread=0.300000
    return dbObj
