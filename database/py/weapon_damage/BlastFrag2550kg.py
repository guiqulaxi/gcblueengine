import pygcb
def CreateDBObject():
    dbObj=pygcb.tcWeaponDamage()
    dbObj.databaseClass='BlastFrag2550kg'
    dbObj.maxRange_m=6624.127930
    dbObj.probDetonate=0.850000
    dbObj.blastCharge_kg=917.806519
    dbObj.fragCharge_kg=790.628967
    dbObj.radCharge_kg=91.780655
    dbObj.fragMetal_kg=841.564514
    dbObj.fragFragment_kg=0.135912
    dbObj.fragSpread=0.300000
    return dbObj
