# -*- coding: utf-8 -*-
import pygcb
def CreateDBObject():
    dbObj=pygcb.tcWeaponDamage()
    dbObj.databaseClass='BlastFragAir21.5kg'
    dbObj.maxRange_m=2916.792969
    dbObj.probDetonate=0.850000
    dbObj.blastCharge_kg=4.823149
    dbObj.fragCharge_kg=9.254567
    dbObj.radCharge_kg=0.482315
    dbObj.fragMetal_kg=7.422284
    dbObj.fragFragment_kg=0.023051
    dbObj.fragSpread=0.200008
    return dbObj
