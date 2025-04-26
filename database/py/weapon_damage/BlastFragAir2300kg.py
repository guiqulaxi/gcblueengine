# -*- coding: utf-8 -*-
import pygcb
def CreateDBObject():
    dbObj=pygcb.tcWeaponDamage()
    dbObj.databaseClass='BlastFragAir2300kg'
    dbObj.maxRange_m=9382.429688
    dbObj.probDetonate=0.850000
    dbObj.blastCharge_kg=250.910965
    dbObj.fragCharge_kg=1166.726074
    dbObj.radCharge_kg=25.091097
    dbObj.fragMetal_kg=882.363037
    dbObj.fragFragment_kg=0.275566
    dbObj.fragSpread=0.300000
    return dbObj
