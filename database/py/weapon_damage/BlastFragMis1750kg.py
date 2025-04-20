import pygcb
def CreateDBObject():
    dbObj=pygcb.tcWeaponDamage()
    dbObj.databaseClass='BlastFragMis1750kg'
    dbObj.maxRange_m=8439.231445
    dbObj.probDetonate=0.850000
    dbObj.blastCharge_kg=202.705948
    dbObj.fragCharge_kg=879.862732
    dbObj.radCharge_kg=20.270594
    dbObj.fragMetal_kg=667.431335
    dbObj.fragFragment_kg=0.217830
    dbObj.fragSpread=0.300000
    return dbObj
