import pygcb
def CreateDBObject():
    dbObj=pygcb.tcWeaponDamage()
    dbObj.databaseClass='BlastFragMis2.3kg'
    dbObj.maxRange_m=1234.961426
    dbObj.probDetonate=0.850000
    dbObj.blastCharge_kg=0.642753
    dbObj.fragCharge_kg=0.905498
    dbObj.radCharge_kg=0.064275
    dbObj.fragMetal_kg=0.751749
    dbObj.fragFragment_kg=0.004475
    dbObj.fragSpread=0.054444
    return dbObj
