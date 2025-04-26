# -*- coding: utf-8 -*-
import pygcb
def CreateDBObject():
    dbObj=pygcb.tcWeaponDamage()
    dbObj.databaseClass='BlastFrag920kg'
    dbObj.maxRange_m=4416.874512
    dbObj.probDetonate=0.850000
    dbObj.blastCharge_kg=331.031677
    dbObj.fragCharge_kg=285.312195
    dbObj.radCharge_kg=33.103168
    dbObj.fragMetal_kg=303.656097
    dbObj.fragFragment_kg=0.057337
    dbObj.fragSpread=0.300000
    return dbObj
