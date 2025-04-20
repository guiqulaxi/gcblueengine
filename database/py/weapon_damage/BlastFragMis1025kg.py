import pygcb
def CreateDBObject():
    dbObj=pygcb.tcWeaponDamage()
    dbObj.databaseClass='BlastFragMis1025kg'
    dbObj.maxRange_m=6763.401367
    dbObj.probDetonate=0.850000
    dbObj.blastCharge_kg=132.250412
    dbObj.fragCharge_kg=506.333069
    dbObj.radCharge_kg=13.225041
    dbObj.fragMetal_kg=386.416534
    dbObj.fragFragment_kg=0.134033
    dbObj.fragSpread=0.300000
    return dbObj
