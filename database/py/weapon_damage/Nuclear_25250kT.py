# -*- coding: utf-8 -*-
import pygcb
def CreateDBObject():
    dbObj=pygcb.tcWeaponDamage()
    dbObj.databaseClass='Nuclear-25250kT'
    dbObj.maxRange_m=83702.492188
    dbObj.probDetonate=0.900000
    dbObj.blastCharge_kg=27775000576.000000
    dbObj.fragCharge_kg=0.000000
    dbObj.radCharge_kg=12625000448.000000
    dbObj.fragMetal_kg=0.000000
    dbObj.fragFragment_kg=0.000000
    dbObj.fragSpread=1.000000
    return dbObj
