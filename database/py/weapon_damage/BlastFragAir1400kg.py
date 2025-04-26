# -*- coding: utf-8 -*-
import pygcb
def CreateDBObject():
    dbObj=pygcb.tcWeaponDamage()
    dbObj.databaseClass='BlastFragAir1400kg'
    dbObj.maxRange_m=7710.133301
    dbObj.probDetonate=0.850000
    dbObj.blastCharge_kg=169.869507
    dbObj.fragCharge_kg=698.753662
    dbObj.radCharge_kg=16.986952
    dbObj.fragMetal_kg=531.376831
    dbObj.fragFragment_kg=0.178494
    dbObj.fragSpread=0.300000
    return dbObj
