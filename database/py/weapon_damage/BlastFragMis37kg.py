import pygcb
def CreateDBObject():
    dbObj=pygcb.tcWeaponDamage()
    dbObj.databaseClass='BlastFragMis37kg'
    dbObj.maxRange_m=3268.678223
    dbObj.probDetonate=0.850000
    dbObj.blastCharge_kg=7.804921
    dbObj.fragCharge_kg=16.256720
    dbObj.radCharge_kg=0.780492
    dbObj.fragMetal_kg=12.938359
    dbObj.fragFragment_kg=0.029010
    dbObj.fragSpread=0.300000
    return dbObj
