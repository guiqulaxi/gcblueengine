import pygcb
def CreateDBObject():
    dbObj=pygcb.tcWeaponDamage()
    dbObj.databaseClass='BlastFragAir640kg'
    dbObj.maxRange_m=5862.320312
    dbObj.probDetonate=0.850000
    dbObj.blastCharge_kg=90.009979
    dbObj.fragCharge_kg=311.193359
    dbObj.radCharge_kg=9.000998
    dbObj.fragMetal_kg=238.796677
    dbObj.fragFragment_kg=0.098392
    dbObj.fragSpread=0.300000
    return dbObj
