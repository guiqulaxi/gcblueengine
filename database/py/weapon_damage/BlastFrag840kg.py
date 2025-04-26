# -*- coding: utf-8 -*-
import pygcb
def CreateDBObject():
    dbObj=pygcb.tcWeaponDamage()
    dbObj.databaseClass='BlastFrag840kg'
    dbObj.maxRange_m=4259.589355
    dbObj.probDetonate=0.850000
    dbObj.blastCharge_kg=302.233948
    dbObj.fragCharge_kg=260.510712
    dbObj.radCharge_kg=30.223392
    dbObj.fragMetal_kg=277.255341
    dbObj.fragFragment_kg=0.053155
    dbObj.fragSpread=0.300000
    return dbObj
