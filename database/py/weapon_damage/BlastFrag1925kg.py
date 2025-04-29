# -*- coding: utf-8 -*-
import pygcb
def CreateDBObject():
    dbObj=pygcb.tcWeaponDamage()
    dbObj.databaseClass='BlastFrag1925kg'
    dbObj.maxRange_m=5914.354004
    dbObj.probDetonate=0.850000
    dbObj.blastCharge_kg=692.813477
    dbObj.fragCharge_kg=596.874329
    dbObj.radCharge_kg=69.281349
    dbObj.fragMetal_kg=635.312195
    dbObj.fragFragment_kg=0.106453
    dbObj.fragSpread=0.300000
    return dbObj
