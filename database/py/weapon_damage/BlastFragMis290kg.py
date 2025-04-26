# -*- coding: utf-8 -*-
import pygcb
def CreateDBObject():
    dbObj=pygcb.tcWeaponDamage()
    dbObj.databaseClass='BlastFragMis290kg'
    dbObj.maxRange_m=4703.554199
    dbObj.probDetonate=0.850000
    dbObj.blastCharge_kg=46.447422
    dbObj.fragCharge_kg=137.235046
    dbObj.radCharge_kg=4.644742
    dbObj.fragMetal_kg=106.317528
    dbObj.fragFragment_kg=0.061562
    dbObj.fragSpread=0.300000
    return dbObj
