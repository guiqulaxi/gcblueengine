# -*- coding: utf-8 -*-
import pygcb
def CreateDBObject():
    dbObj=pygcb.tcWeaponDamage()
    dbObj.databaseClass='BlastFragMis375kg'
    dbObj.maxRange_m=5042.081543
    dbObj.probDetonate=0.850000
    dbObj.blastCharge_kg=57.684006
    dbObj.fragCharge_kg=179.043991
    dbObj.radCharge_kg=5.768401
    dbObj.fragMetal_kg=138.272003
    dbObj.fragFragment_kg=0.071311
    dbObj.fragSpread=0.300000
    return dbObj
