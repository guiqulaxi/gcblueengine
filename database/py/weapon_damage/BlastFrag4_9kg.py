import pygcb
def CreateDBObject():
    dbObj=pygcb.tcWeaponDamage()
    dbObj.databaseClass='BlastFrag4.9kg'
    dbObj.maxRange_m=391.665894
    dbObj.probDetonate=0.850000
    dbObj.blastCharge_kg=1.724805
    dbObj.fragCharge_kg=1.545130
    dbObj.radCharge_kg=0.172480
    dbObj.fragMetal_kg=1.630065
    dbObj.fragFragment_kg=0.000760
    dbObj.fragSpread=0.300000
    return dbObj
