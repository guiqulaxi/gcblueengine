import pygcb
def CreateDBObject():
    dbObj=pygcb.tcWeaponDamage()
    dbObj.databaseClass='BlastFragMis440kg'
    dbObj.maxRange_m=5242.208008
    dbObj.probDetonate=0.850000
    dbObj.blastCharge_kg=65.947929
    dbObj.fragCharge_kg=211.234711
    dbObj.radCharge_kg=6.594793
    dbObj.fragMetal_kg=162.817352
    dbObj.fragFragment_kg=0.077458
    dbObj.fragSpread=0.300000
    return dbObj
