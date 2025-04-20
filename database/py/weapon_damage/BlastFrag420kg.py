import pygcb
def CreateDBObject():
    dbObj=pygcb.tcWeaponDamage()
    dbObj.databaseClass='BlastFrag420kg'
    dbObj.maxRange_m=3160.737793
    dbObj.probDetonate=0.850000
    dbObj.blastCharge_kg=151.051025
    dbObj.fragCharge_kg=130.299316
    dbObj.radCharge_kg=15.105103
    dbObj.fragMetal_kg=138.649658
    dbObj.fragFragment_kg=0.028789
    dbObj.fragSpread=0.300000
    return dbObj
