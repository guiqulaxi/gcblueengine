import pygcb
def CreateDBObject():
    dbObj=pygcb.tcWeaponDamage()
    dbObj.databaseClass='BlastFragMis4.4kg'
    dbObj.maxRange_m=1682.670288
    dbObj.probDetonate=0.850000
    dbObj.blastCharge_kg=1.159220
    dbObj.fragCharge_kg=1.779186
    dbObj.radCharge_kg=0.115922
    dbObj.fragMetal_kg=1.461593
    dbObj.fragFragment_kg=0.007901
    dbObj.fragSpread=0.066020
    return dbObj
