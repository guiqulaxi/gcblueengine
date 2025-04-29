# -*- coding: utf-8 -*-
import pygcb
def CreateDBObject():
    dbObj=pygcb.tcWeaponDamage()
    dbObj.databaseClass='BlastFragAir7.8kg'
    dbObj.maxRange_m=2130.232178
    dbObj.probDetonate=0.850000
    dbObj.blastCharge_kg=1.944845
    dbObj.fragCharge_kg=3.227437
    dbObj.radCharge_kg=0.194484
    dbObj.fragMetal_kg=2.627718
    dbObj.fragFragment_kg=0.012395
    dbObj.fragSpread=0.086698
    return dbObj
