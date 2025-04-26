# -*- coding: utf-8 -*-
import pygcb
def CreateDBObject():
    dbObj=pygcb.tcWeaponDamage()
    dbObj.databaseClass='BlastFrag2900kg'
    dbObj.maxRange_m=6970.851074
    dbObj.probDetonate=0.850000
    dbObj.blastCharge_kg=1043.803345
    dbObj.fragCharge_kg=899.131104
    dbObj.radCharge_kg=104.380341
    dbObj.fragMetal_kg=957.065552
    dbObj.fragFragment_kg=0.151819
    dbObj.fragSpread=0.300000
    return dbObj
