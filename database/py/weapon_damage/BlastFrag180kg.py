# -*- coding: utf-8 -*-
import pygcb
def CreateDBObject():
    dbObj=pygcb.tcWeaponDamage()
    dbObj.databaseClass='BlastFrag180kg'
    dbObj.maxRange_m=2238.578857
    dbObj.probDetonate=0.850000
    dbObj.blastCharge_kg=64.671928
    dbObj.fragCharge_kg=55.885384
    dbObj.radCharge_kg=6.467193
    dbObj.fragMetal_kg=59.442692
    dbObj.fragFragment_kg=0.014512
    dbObj.fragSpread=0.300000
    return dbObj
