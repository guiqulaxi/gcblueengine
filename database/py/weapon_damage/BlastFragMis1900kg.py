# -*- coding: utf-8 -*-
import pygcb
def CreateDBObject():
    dbObj=pygcb.tcWeaponDamage()
    dbObj.databaseClass='BlastFragMis1900kg'
    dbObj.maxRange_m=8716.994141
    dbObj.probDetonate=0.850000
    dbObj.blastCharge_kg=216.227081
    dbObj.fragCharge_kg=957.848633
    dbObj.radCharge_kg=21.622707
    dbObj.fragMetal_kg=725.924316
    dbObj.fragFragment_kg=0.234018
    dbObj.fragSpread=0.300000
    return dbObj
