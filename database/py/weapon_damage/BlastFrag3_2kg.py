import pygcb
def CreateDBObject():
    dbObj=pygcb.tcWeaponDamage()
    dbObj.databaseClass='BlastFrag3.2kg'
    dbObj.maxRange_m=315.878357
    dbObj.probDetonate=0.850000
    dbObj.blastCharge_kg=1.123313
    dbObj.fragCharge_kg=1.011125
    dbObj.radCharge_kg=0.112331
    dbObj.fragMetal_kg=1.065562
    dbObj.fragFragment_kg=0.000569
    dbObj.fragSpread=0.300000
    return dbObj
