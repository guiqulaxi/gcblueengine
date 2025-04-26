# -*- coding: utf-8 -*-
import pygcb
def CreateDBObject():
    dbObj=pygcb.tcWeaponDamage()
    dbObj.databaseClass='Nuclear-13250kT'
    dbObj.maxRange_m=68980.250000
    dbObj.probDetonate=0.900000
    dbObj.blastCharge_kg=14574999552.000000
    dbObj.fragCharge_kg=0.000000
    dbObj.radCharge_kg=6624999936.000000
    dbObj.fragMetal_kg=0.000000
    dbObj.fragFragment_kg=0.000000
    dbObj.fragSpread=1.000000
    return dbObj
