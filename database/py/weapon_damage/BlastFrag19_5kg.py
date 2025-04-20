import pygcb
def CreateDBObject():
    dbObj=pygcb.tcWeaponDamage()
    dbObj.databaseClass='BlastFrag19.5kg'
    dbObj.maxRange_m=798.930237
    dbObj.probDetonate=0.850000
    dbObj.blastCharge_kg=6.946741
    dbObj.fragCharge_kg=6.093840
    dbObj.radCharge_kg=0.694674
    dbObj.fragMetal_kg=6.459420
    dbObj.fragFragment_kg=0.002255
    dbObj.fragSpread=0.300000
    return dbObj
