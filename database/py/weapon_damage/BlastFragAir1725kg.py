# -*- coding: utf-8 -*-
import pygcb
def CreateDBObject():
    dbObj=pygcb.tcWeaponDamage()
    dbObj.databaseClass='BlastFragAir1725kg'
    dbObj.maxRange_m=8390.743164
    dbObj.probDetonate=0.850000
    dbObj.blastCharge_kg=200.422302
    dbObj.fragCharge_kg=866.885132
    dbObj.radCharge_kg=20.042231
    dbObj.fragMetal_kg=657.692566
    dbObj.fragFragment_kg=0.215073
    dbObj.fragSpread=0.300000
    return dbObj
