import pygcb
def CreateDBObject():
    dbObj=pygcb.tcWeaponDamage()
    dbObj.databaseClass='BlastFragMis3400kg'
    dbObj.maxRange_m=10809.699219
    dbObj.probDetonate=0.850000
    dbObj.blastCharge_kg=338.136047
    dbObj.fragCharge_kg=1746.575928
    dbObj.radCharge_kg=33.813602
    dbObj.fragMetal_kg=1315.287964
    dbObj.fragFragment_kg=0.378282
    dbObj.fragSpread=0.300000
    return dbObj
