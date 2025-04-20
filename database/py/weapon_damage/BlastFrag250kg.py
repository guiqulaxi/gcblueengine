import pygcb
def CreateDBObject():
    dbObj=pygcb.tcWeaponDamage()
    dbObj.databaseClass='BlastFrag250kg'
    dbObj.maxRange_m=2575.451660
    dbObj.probDetonate=0.850000
    dbObj.blastCharge_kg=89.863823
    dbObj.fragCharge_kg=77.590782
    dbObj.radCharge_kg=8.986382
    dbObj.fragMetal_kg=82.545395
    dbObj.fragFragment_kg=0.019108
    dbObj.fragSpread=0.300000
    return dbObj
