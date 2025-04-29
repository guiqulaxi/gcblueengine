# -*- coding: utf-8 -*-
import pygcb
def CreateDBObject():
    dbObj=pygcb.tcWeaponDamage()
    dbObj.databaseClass='BlastFragMis980kg'
    dbObj.maxRange_m=6655.181641
    dbObj.probDetonate=0.850000
    dbObj.blastCharge_kg=127.529411
    dbObj.fragCharge_kg=483.380402
    dbObj.radCharge_kg=12.752941
    dbObj.fragMetal_kg=369.090210
    dbObj.fragFragment_kg=0.129415
    dbObj.fragSpread=0.300000
    return dbObj
