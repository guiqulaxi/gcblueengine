import pygcb
def CreateDBObject():
    dbObj=pygcb.tcWeaponDamage()
    dbObj.databaseClass='BlastFrag4000kg'
    dbObj.maxRange_m=7878.298828
    dbObj.probDetonate=0.850000
    dbObj.blastCharge_kg=1439.795410
    dbObj.fragCharge_kg=1240.136353
    dbObj.radCharge_kg=143.979538
    dbObj.fragMetal_kg=1320.068237
    dbObj.fragFragment_kg=0.198328
    dbObj.fragSpread=0.300000
    return dbObj
