import pygcb
def CreateDBObject():
    dbObj=pygcb.tcWeaponDamage()
    dbObj.databaseClass='BlastFrag17.5kg'
    dbObj.maxRange_m=758.508240
    dbObj.probDetonate=0.850000
    dbObj.blastCharge_kg=6.229409
    dbObj.fragCharge_kg=5.472060
    dbObj.radCharge_kg=0.622941
    dbObj.fragMetal_kg=5.798530
    dbObj.fragFragment_kg=0.002071
    dbObj.fragSpread=0.300000
    return dbObj
