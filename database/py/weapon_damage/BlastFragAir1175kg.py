# -*- coding: utf-8 -*-
import pygcb
def CreateDBObject():
    dbObj=pygcb.tcWeaponDamage()
    dbObj.databaseClass='BlastFragAir1175kg'
    dbObj.maxRange_m=7168.304688
    dbObj.probDetonate=0.850000
    dbObj.blastCharge_kg=147.646301
    dbObj.fragCharge_kg=583.069153
    dbObj.radCharge_kg=14.764630
    dbObj.fragMetal_kg=444.284576
    dbObj.fragFragment_kg=0.152152
    dbObj.fragSpread=0.300000
    return dbObj
