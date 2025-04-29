# -*- coding: utf-8 -*-
import pygcb
def CreateDBObject():
    dbObj=pygcb.tcWeaponDamage()
    dbObj.databaseClass='BlastFrag175kg'
    dbObj.maxRange_m=2210.842041
    dbObj.probDetonate=0.850000
    dbObj.blastCharge_kg=62.872620
    dbObj.fragCharge_kg=54.334919
    dbObj.radCharge_kg=6.287262
    dbObj.fragMetal_kg=57.792461
    dbObj.fragFragment_kg=0.014165
    dbObj.fragSpread=0.300000
    return dbObj
