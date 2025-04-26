# -*- coding: utf-8 -*-
import pygcb
def CreateDBObject():
    dbObj=pygcb.tcWeaponDamage()
    dbObj.databaseClass='BlastFragAir2350kg'
    dbObj.maxRange_m=9459.509766
    dbObj.probDetonate=0.850000
    dbObj.blastCharge_kg=255.119095
    dbObj.fragCharge_kg=1192.920654
    dbObj.radCharge_kg=25.511909
    dbObj.fragMetal_kg=901.960327
    dbObj.fragFragment_kg=0.280635
    dbObj.fragSpread=0.300000
    return dbObj
