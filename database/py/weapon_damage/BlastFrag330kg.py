import pygcb
def CreateDBObject():
    dbObj=pygcb.tcWeaponDamage()
    dbObj.databaseClass='BlastFrag330kg'
    dbObj.maxRange_m=2876.235840
    dbObj.probDetonate=0.850000
    dbObj.blastCharge_kg=118.656975
    dbObj.fragCharge_kg=102.395348
    dbObj.radCharge_kg=11.865698
    dbObj.fragMetal_kg=108.947678
    dbObj.fragFragment_kg=0.023808
    dbObj.fragSpread=0.300000
    return dbObj
