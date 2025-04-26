# -*- coding: utf-8 -*-
import pygcb
def CreateDBObject():
    dbObj=pygcb.tcWeaponDamage()
    dbObj.databaseClass='BlastFragAir325kg'
    dbObj.maxRange_m=4855.963867
    dbObj.probDetonate=0.850000
    dbObj.blastCharge_kg=51.139828
    dbObj.fragCharge_kg=154.406784
    dbObj.radCharge_kg=5.113983
    dbObj.fragMetal_kg=119.453392
    dbObj.fragFragment_kg=0.065851
    dbObj.fragSpread=0.300000
    return dbObj
