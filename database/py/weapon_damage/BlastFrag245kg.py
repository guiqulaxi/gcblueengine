import pygcb
def CreateDBObject():
    dbObj=pygcb.tcWeaponDamage()
    dbObj.databaseClass='BlastFrag245kg'
    dbObj.maxRange_m=2554.076660
    dbObj.probDetonate=0.850000
    dbObj.blastCharge_kg=88.064323
    dbObj.fragCharge_kg=76.040451
    dbObj.radCharge_kg=8.806432
    dbObj.fragMetal_kg=80.895226
    dbObj.fragFragment_kg=0.018795
    dbObj.fragSpread=0.300000
    return dbObj
