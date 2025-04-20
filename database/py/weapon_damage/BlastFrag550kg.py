import pygcb
def CreateDBObject():
    dbObj=pygcb.tcWeaponDamage()
    dbObj.databaseClass='BlastFrag550kg'
    dbObj.maxRange_m=3561.866455
    dbObj.probDetonate=0.850000
    dbObj.blastCharge_kg=197.844376
    dbObj.fragCharge_kg=170.603745
    dbObj.radCharge_kg=19.784437
    dbObj.fragMetal_kg=181.551880
    dbObj.fragFragment_kg=0.036722
    dbObj.fragSpread=0.300000
    return dbObj
