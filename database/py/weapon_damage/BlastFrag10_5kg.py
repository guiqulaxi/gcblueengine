import pygcb
def CreateDBObject():
    dbObj=pygcb.tcWeaponDamage()
    dbObj.databaseClass='BlastFrag10.5kg'
    dbObj.maxRange_m=580.085083
    dbObj.probDetonate=0.850000
    dbObj.blastCharge_kg=3.722008
    dbObj.fragCharge_kg=3.293661
    dbObj.radCharge_kg=0.372201
    dbObj.fragMetal_kg=3.484331
    dbObj.fragFragment_kg=0.001353
    dbObj.fragSpread=0.300000
    return dbObj
