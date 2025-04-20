import pygcb
def CreateDBObject():
    dbObj=pygcb.tcWeaponDamage()
    dbObj.databaseClass='BlastFragMis280kg'
    dbObj.maxRange_m=4656.278320
    dbObj.probDetonate=0.850000
    dbObj.blastCharge_kg=45.088116
    dbObj.fragCharge_kg=132.341263
    dbObj.radCharge_kg=4.508811
    dbObj.fragMetal_kg=102.570625
    dbObj.fragFragment_kg=0.060265
    dbObj.fragSpread=0.300000
    return dbObj
