import pygcb
def CreateDBObject():
    dbObj=pygcb.tcWeaponDamage()
    dbObj.databaseClass='BlastFrag9.2kg'
    dbObj.maxRange_m=543.287231
    dbObj.probDetonate=0.850000
    dbObj.blastCharge_kg=3.257268
    dbObj.fragCharge_kg=2.888488
    dbObj.radCharge_kg=0.325727
    dbObj.fragMetal_kg=3.054244
    dbObj.fragFragment_kg=0.001224
    dbObj.fragSpread=0.300000
    return dbObj
