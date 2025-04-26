# -*- coding: utf-8 -*-
import pygcb
def CreateDBObject():
    dbObj=pygcb.tcWeaponDamage()
    dbObj.databaseClass='BlastFragAir22kg'
    dbObj.maxRange_m=2933.090088
    dbObj.probDetonate=0.850000
    dbObj.blastCharge_kg=4.922841
    dbObj.fragCharge_kg=9.478106
    dbObj.radCharge_kg=0.492284
    dbObj.fragMetal_kg=7.599053
    dbObj.fragFragment_kg=0.023310
    dbObj.fragSpread=0.205008
    return dbObj
