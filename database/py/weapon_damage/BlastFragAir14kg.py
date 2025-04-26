# -*- coding: utf-8 -*-
import pygcb
def CreateDBObject():
    dbObj=pygcb.tcWeaponDamage()
    dbObj.databaseClass='BlastFragAir14kg'
    dbObj.maxRange_m=2595.346191
    dbObj.probDetonate=0.850000
    dbObj.blastCharge_kg=3.288780
    dbObj.fragCharge_kg=5.927480
    dbObj.radCharge_kg=0.328878
    dbObj.fragMetal_kg=4.783740
    dbObj.fragFragment_kg=0.018259
    dbObj.fragSpread=0.132415
    return dbObj
