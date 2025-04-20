import pygcb
def CreateDBObject():
    dbObj=pygcb.tcWeaponDamage()
    dbObj.databaseClass='BlastFragMis0.2kg'
    dbObj.maxRange_m=499.145233
    dbObj.probDetonate=0.850000
    dbObj.blastCharge_kg=0.060000
    dbObj.fragCharge_kg=0.076000
    dbObj.radCharge_kg=0.006000
    dbObj.fragMetal_kg=0.064000
    dbObj.fragFragment_kg=0.001000
    dbObj.fragSpread=0.007901
    return dbObj
