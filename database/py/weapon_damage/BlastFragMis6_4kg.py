import pygcb
def CreateDBObject():
    dbObj=pygcb.tcWeaponDamage()
    dbObj.databaseClass='BlastFragMis6.4kg'
    dbObj.maxRange_m=1971.510254
    dbObj.probDetonate=0.850000
    dbObj.blastCharge_kg=1.626996
    dbObj.fragCharge_kg=2.627336
    dbObj.radCharge_kg=0.162700
    dbObj.fragMetal_kg=2.145668
    dbObj.fragFragment_kg=0.010675
    dbObj.fragSpread=0.077934
    return dbObj
