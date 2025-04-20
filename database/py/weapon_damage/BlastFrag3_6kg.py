import pygcb
def CreateDBObject():
    dbObj=pygcb.tcWeaponDamage()
    dbObj.databaseClass='BlastFrag3.6kg'
    dbObj.maxRange_m=336.720001
    dbObj.probDetonate=0.850000
    dbObj.blastCharge_kg=1.264408
    dbObj.fragCharge_kg=1.137061
    dbObj.radCharge_kg=0.126441
    dbObj.fragMetal_kg=1.198531
    dbObj.fragFragment_kg=0.000619
    dbObj.fragSpread=0.300000
    return dbObj
