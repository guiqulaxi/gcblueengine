# -*- coding: utf-8 -*-
import pygcb
def CreateDBObject():
    dbObj=pygcb.tcWeaponDamage()
    dbObj.databaseClass='BlastFrag20.5kg'
    dbObj.maxRange_m=817.855896
    dbObj.probDetonate=0.850000
    dbObj.blastCharge_kg=7.305507
    dbObj.fragCharge_kg=6.404662
    dbObj.radCharge_kg=0.730551
    dbObj.fragMetal_kg=6.789831
    dbObj.fragFragment_kg=0.002345
    dbObj.fragSpread=0.300000
    return dbObj
