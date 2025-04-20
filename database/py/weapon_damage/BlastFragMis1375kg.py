import pygcb
def CreateDBObject():
    dbObj=pygcb.tcWeaponDamage()
    dbObj.databaseClass='BlastFragMis1375kg'
    dbObj.maxRange_m=7653.983398
    dbObj.probDetonate=0.850000
    dbObj.blastCharge_kg=167.447159
    dbObj.fragCharge_kg=685.868530
    dbObj.radCharge_kg=16.744717
    dbObj.fragMetal_kg=521.684265
    dbObj.fragFragment_kg=0.175651
    dbObj.fragSpread=0.300000
    return dbObj
