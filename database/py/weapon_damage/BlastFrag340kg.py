import pygcb
def CreateDBObject():
    dbObj=pygcb.tcWeaponDamage()
    dbObj.databaseClass='BlastFrag340kg'
    dbObj.maxRange_m=2909.238281
    dbObj.probDetonate=0.850000
    dbObj.blastCharge_kg=122.256241
    dbObj.fragCharge_kg=105.495842
    dbObj.radCharge_kg=12.225624
    dbObj.fragMetal_kg=112.247917
    dbObj.fragFragment_kg=0.024359
    dbObj.fragSpread=0.300000
    return dbObj
