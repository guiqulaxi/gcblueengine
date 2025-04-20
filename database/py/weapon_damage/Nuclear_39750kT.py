import pygcb
def CreateDBObject():
    dbObj=pygcb.tcWeaponDamage()
    dbObj.databaseClass='Nuclear-39750kT'
    dbObj.maxRange_m=95909.390625
    dbObj.probDetonate=0.900000
    dbObj.blastCharge_kg=43725000704.000000
    dbObj.fragCharge_kg=0.000000
    dbObj.radCharge_kg=19875000320.000000
    dbObj.fragMetal_kg=0.000000
    dbObj.fragFragment_kg=0.000000
    dbObj.fragSpread=1.000000
    return dbObj
