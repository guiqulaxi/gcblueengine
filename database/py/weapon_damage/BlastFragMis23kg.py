import pygcb
def CreateDBObject():
    dbObj=pygcb.tcWeaponDamage()
    dbObj.databaseClass='BlastFragMis23kg'
    dbObj.maxRange_m=2964.284912
    dbObj.probDetonate=0.850000
    dbObj.blastCharge_kg=5.121392
    dbObj.fragCharge_kg=9.925739
    dbObj.radCharge_kg=0.512139
    dbObj.fragMetal_kg=7.952869
    dbObj.fragFragment_kg=0.023811
    dbObj.fragSpread=0.215193
    return dbObj
