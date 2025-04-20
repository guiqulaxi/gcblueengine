import pygcb
def CreateDBObject():
    dbObj=pygcb.tcWeaponDamage()
    dbObj.databaseClass='BlastFrag4.3kg'
    dbObj.maxRange_m=368.384521
    dbObj.probDetonate=0.850000
    dbObj.blastCharge_kg=1.512026
    dbObj.fragCharge_kg=1.356983
    dbObj.radCharge_kg=0.151203
    dbObj.fragMetal_kg=1.430991
    dbObj.fragFragment_kg=0.000699
    dbObj.fragSpread=0.300000
    return dbObj
