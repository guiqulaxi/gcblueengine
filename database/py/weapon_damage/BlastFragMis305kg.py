import pygcb
def CreateDBObject():
    dbObj=pygcb.tcWeaponDamage()
    dbObj.databaseClass='BlastFragMis305kg'
    dbObj.maxRange_m=4771.713867
    dbObj.probDetonate=0.850000
    dbObj.blastCharge_kg=48.470524
    dbObj.fragCharge_kg=144.586319
    dbObj.radCharge_kg=4.847053
    dbObj.fragMetal_kg=111.943161
    dbObj.fragFragment_kg=0.063460
    dbObj.fragSpread=0.300000
    return dbObj
