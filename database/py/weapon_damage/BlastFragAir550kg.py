# -*- coding: utf-8 -*-
import pygcb
def CreateDBObject():
    dbObj=pygcb.tcWeaponDamage()
    dbObj.databaseClass='BlastFragAir550kg'
    dbObj.maxRange_m=5576.604492
    dbObj.probDetonate=0.850000
    dbObj.blastCharge_kg=79.408051
    dbObj.fragCharge_kg=266.061310
    dbObj.radCharge_kg=7.940804
    dbObj.fragMetal_kg=204.530655
    dbObj.fragFragment_kg=0.088388
    dbObj.fragSpread=0.300000
    return dbObj
