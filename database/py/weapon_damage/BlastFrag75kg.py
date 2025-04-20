import pygcb
def CreateDBObject():
    dbObj=pygcb.tcWeaponDamage()
    dbObj.databaseClass='BlastFrag75kg'
    dbObj.maxRange_m=1492.867188
    dbObj.probDetonate=0.850000
    dbObj.blastCharge_kg=26.893518
    dbObj.fragCharge_kg=23.320988
    dbObj.radCharge_kg=2.689352
    dbObj.fragMetal_kg=24.785494
    dbObj.fragFragment_kg=0.006735
    dbObj.fragSpread=0.300000
    return dbObj
