# -*- coding: utf-8 -*-
import pygcb
def CreateDBObject():
    dbObj=pygcb.tcWeaponDamage()
    dbObj.databaseClass='BlastFragMis4.2kg'
    dbObj.maxRange_m=1649.991821
    dbObj.probDetonate=0.850000
    dbObj.blastCharge_kg=1.111347
    dbObj.fragCharge_kg=1.695102
    dbObj.radCharge_kg=0.111135
    dbObj.fragMetal_kg=1.393551
    dbObj.fragFragment_kg=0.007615
    dbObj.fragSpread=0.064601
    return dbObj
