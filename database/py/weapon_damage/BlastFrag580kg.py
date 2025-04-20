import pygcb
def CreateDBObject():
    dbObj=pygcb.tcWeaponDamage()
    dbObj.databaseClass='BlastFrag580kg'
    dbObj.maxRange_m=3643.774170
    dbObj.probDetonate=0.850000
    dbObj.blastCharge_kg=208.643066
    dbObj.fragCharge_kg=179.904617
    dbObj.radCharge_kg=20.864307
    dbObj.fragMetal_kg=191.452316
    dbObj.fragFragment_kg=0.038475
    dbObj.fragSpread=0.300000
    return dbObj
