import pygcb
def CreateDBObject():
    dbObj=pygcb.tcWeaponDamage()
    dbObj.databaseClass='BlastFrag9.8kg'
    dbObj.maxRange_m=559.191345
    dbObj.probDetonate=0.850000
    dbObj.blastCharge_kg=3.471709
    dbObj.fragCharge_kg=3.075527
    dbObj.radCharge_kg=0.347171
    dbObj.fragMetal_kg=3.252764
    dbObj.fragFragment_kg=0.001279
    dbObj.fragSpread=0.300000
    return dbObj
