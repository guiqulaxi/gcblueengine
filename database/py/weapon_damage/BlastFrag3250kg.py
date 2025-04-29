# -*- coding: utf-8 -*-
import pygcb
def CreateDBObject():
    dbObj=pygcb.tcWeaponDamage()
    dbObj.databaseClass='BlastFrag3250kg'
    dbObj.maxRange_m=7286.166992
    dbObj.probDetonate=0.850000
    dbObj.blastCharge_kg=1169.800537
    dbObj.fragCharge_kg=1007.632935
    dbObj.radCharge_kg=116.980057
    dbObj.fragMetal_kg=1072.566528
    dbObj.fragFragment_kg=0.167171
    dbObj.fragSpread=0.300000
    return dbObj
