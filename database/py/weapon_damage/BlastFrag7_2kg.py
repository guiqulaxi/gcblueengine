import pygcb
def CreateDBObject():
    dbObj=pygcb.tcWeaponDamage()
    dbObj.databaseClass='BlastFrag7.2kg'
    dbObj.maxRange_m=482.268707
    dbObj.probDetonate=0.850000
    dbObj.blastCharge_kg=2.543313
    dbObj.fragCharge_kg=2.264458
    dbObj.radCharge_kg=0.254331
    dbObj.fragMetal_kg=2.392229
    dbObj.fragFragment_kg=0.001024
    dbObj.fragSpread=0.300000
    return dbObj
