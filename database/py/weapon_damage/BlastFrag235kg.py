import pygcb
def CreateDBObject():
    dbObj=pygcb.tcWeaponDamage()
    dbObj.databaseClass='BlastFrag235kg'
    dbObj.maxRange_m=2510.237549
    dbObj.probDetonate=0.850000
    dbObj.blastCharge_kg=84.465347
    dbObj.fragCharge_kg=72.939766
    dbObj.radCharge_kg=8.446535
    dbObj.fragMetal_kg=77.594887
    dbObj.fragFragment_kg=0.018164
    dbObj.fragSpread=0.300000
    return dbObj
