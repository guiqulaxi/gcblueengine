import pygcb
def CreateDBObject():
    dbObj=pygcb.tcWeaponDamage()
    dbObj.databaseClass='BlastFragMis110kg'
    dbObj.maxRange_m=3941.010986
    dbObj.probDetonate=0.850000
    dbObj.blastCharge_kg=20.247908
    dbObj.fragCharge_kg=50.301395
    dbObj.radCharge_kg=2.024791
    dbObj.fragMetal_kg=39.450699
    dbObj.fragFragment_kg=0.042557
    dbObj.fragSpread=0.300000
    return dbObj
