import pygcb
def CreateDBObject():
    dbObj=pygcb.tcWeaponDamage()
    dbObj.databaseClass='BlastFragAir350kg'
    dbObj.maxRange_m=4952.415527
    dbObj.probDetonate=0.850000
    dbObj.blastCharge_kg=54.433956
    dbObj.fragCharge_kg=166.710693
    dbObj.radCharge_kg=5.443396
    dbObj.fragMetal_kg=128.855347
    dbObj.fragFragment_kg=0.068650
    dbObj.fragSpread=0.300000
    return dbObj
