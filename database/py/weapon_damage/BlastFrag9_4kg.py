# -*- coding: utf-8 -*-
import pygcb
def CreateDBObject():
    dbObj=pygcb.tcWeaponDamage()
    dbObj.databaseClass='BlastFrag9.4kg'
    dbObj.maxRange_m=548.695984
    dbObj.probDetonate=0.850000
    dbObj.blastCharge_kg=3.328737
    dbObj.fragCharge_kg=2.950842
    dbObj.radCharge_kg=0.332874
    dbObj.fragMetal_kg=3.120421
    dbObj.fragFragment_kg=0.001242
    dbObj.fragSpread=0.300000
    return dbObj
