import pygcb
def CreateDBObject():
    dbObj=pygcb.tcWeaponDamage()
    dbObj.databaseClass='BlastFragMis500kg'
    dbObj.maxRange_m=5396.381348
    dbObj.probDetonate=0.850000
    dbObj.blastCharge_kg=73.364456
    dbObj.fragCharge_kg=241.090363
    dbObj.radCharge_kg=7.336445
    dbObj.fragMetal_kg=185.545181
    dbObj.fragFragment_kg=0.082391
    dbObj.fragSpread=0.300000
    return dbObj
