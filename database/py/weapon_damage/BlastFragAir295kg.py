# -*- coding: utf-8 -*-
import pygcb
def CreateDBObject():
    dbObj=pygcb.tcWeaponDamage()
    dbObj.databaseClass='BlastFragAir295kg'
    dbObj.maxRange_m=4727.141113
    dbObj.probDetonate=0.850000
    dbObj.blastCharge_kg=47.123871
    dbObj.fragCharge_kg=139.684082
    dbObj.radCharge_kg=4.712387
    dbObj.fragMetal_kg=108.192047
    dbObj.fragFragment_kg=0.062215
    dbObj.fragSpread=0.300000
    return dbObj
