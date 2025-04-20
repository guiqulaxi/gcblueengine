import pygcb
def CreateDBObject():
    dbObj=pygcb.tcWeaponDamage()
    dbObj.databaseClass='BlastFragAir3.3kg'
    dbObj.maxRange_m=1475.263184
    dbObj.probDetonate=0.850000
    dbObj.blastCharge_kg=0.892829
    dbObj.fragCharge_kg=1.318781
    dbObj.radCharge_kg=0.089283
    dbObj.fragMetal_kg=1.088390
    dbObj.fragFragment_kg=0.006184
    dbObj.fragSpread=0.059753
    return dbObj
