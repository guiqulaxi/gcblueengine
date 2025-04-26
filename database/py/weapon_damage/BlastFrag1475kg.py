# -*- coding: utf-8 -*-
import pygcb
def CreateDBObject():
    dbObj=pygcb.tcWeaponDamage()
    dbObj.databaseClass='BlastFrag1475kg'
    dbObj.maxRange_m=5343.761719
    dbObj.probDetonate=0.850000
    dbObj.blastCharge_kg=530.820068
    dbObj.fragCharge_kg=457.369965
    dbObj.radCharge_kg=53.082005
    dbObj.fragMetal_kg=486.809998
    dbObj.fragFragment_kg=0.085706
    dbObj.fragSpread=0.300000
    return dbObj
