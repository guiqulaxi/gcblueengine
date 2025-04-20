import pygcb
def CreateDBObject():
    dbObj=pygcb.tcWeaponDamage()
    dbObj.databaseClass='BlastFrag15.5kg'
    dbObj.maxRange_m=714.145569
    dbObj.probDetonate=0.850000
    dbObj.blastCharge_kg=5.512403
    dbObj.fragCharge_kg=4.850065
    dbObj.radCharge_kg=0.551240
    dbObj.fragMetal_kg=5.137533
    dbObj.fragFragment_kg=0.001878
    dbObj.fragSpread=0.300000
    return dbObj
