# -*- coding: utf-8 -*-
import pygcb
def CreateDBObject():
    dbObj=pygcb.tcWeaponDamage()
    dbObj.databaseClass='BlastFragMis42kg'
    dbObj.maxRange_m=3340.005615
    dbObj.probDetonate=0.850000
    dbObj.blastCharge_kg=8.728345
    dbObj.fragCharge_kg=18.541103
    dbObj.radCharge_kg=0.872834
    dbObj.fragMetal_kg=14.730552
    dbObj.fragFragment_kg=0.030310
    dbObj.fragSpread=0.300000
    return dbObj
