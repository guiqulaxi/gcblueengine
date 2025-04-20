import pygcb
def CreateDBObject():
    dbObj=pygcb.tcWeaponDamage()
    dbObj.databaseClass='BlastFrag2600kg'
    dbObj.maxRange_m=6675.821289
    dbObj.probDetonate=0.850000
    dbObj.blastCharge_kg=935.806091
    dbObj.fragCharge_kg=806.129272
    dbObj.radCharge_kg=93.580605
    dbObj.fragMetal_kg=858.064636
    dbObj.fragFragment_kg=0.138219
    dbObj.fragSpread=0.300000
    return dbObj
