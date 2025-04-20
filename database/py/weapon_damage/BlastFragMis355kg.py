import pygcb
def CreateDBObject():
    dbObj=pygcb.tcWeaponDamage()
    dbObj.databaseClass='BlastFragMis355kg'
    dbObj.maxRange_m=4971.452148
    dbObj.probDetonate=0.850000
    dbObj.blastCharge_kg=55.087395
    dbObj.fragCharge_kg=169.175064
    dbObj.radCharge_kg=5.508739
    dbObj.fragMetal_kg=130.737534
    dbObj.fragFragment_kg=0.069210
    dbObj.fragSpread=0.300000
    return dbObj
