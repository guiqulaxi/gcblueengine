# -*- coding: utf-8 -*-
import pygcb
def CreateDBObject():
    dbObj=pygcb.tcWeaponDamage()
    dbObj.databaseClass='BlastFrag3950kg'
    dbObj.maxRange_m=7841.846680
    dbObj.probDetonate=0.850000
    dbObj.blastCharge_kg=1421.795776
    dbObj.fragCharge_kg=1224.636108
    dbObj.radCharge_kg=142.179581
    dbObj.fragMetal_kg=1303.568115
    dbObj.fragFragment_kg=0.196320
    dbObj.fragSpread=0.300000
    return dbObj
