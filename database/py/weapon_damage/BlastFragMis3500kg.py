import pygcb
def CreateDBObject():
    dbObj=pygcb.tcWeaponDamage()
    dbObj.databaseClass='BlastFragMis3500kg'
    dbObj.maxRange_m=10918.135742
    dbObj.probDetonate=0.850000
    dbObj.blastCharge_kg=345.579010
    dbObj.fragCharge_kg=1799.614014
    dbObj.radCharge_kg=34.557899
    dbObj.fragMetal_kg=1354.807007
    dbObj.fragFragment_kg=0.386867
    dbObj.fragSpread=0.300000
    return dbObj
