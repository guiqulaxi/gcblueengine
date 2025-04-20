import pygcb
def CreateDBObject():
    dbObj=pygcb.tcWeaponDamage()
    dbObj.databaseClass='BlastFrag220kg'
    dbObj.maxRange_m=2441.572510
    dbObj.probDetonate=0.850000
    dbObj.blastCharge_kg=79.066978
    dbObj.fragCharge_kg=68.288681
    dbObj.radCharge_kg=7.906698
    dbObj.fragMetal_kg=72.644341
    dbObj.fragFragment_kg=0.017198
    dbObj.fragSpread=0.300000
    return dbObj
