import pygcb
def CreateDBObject():
    dbObj=pygcb.tcWeaponDamage()
    dbObj.databaseClass='BlastFrag900kg'
    dbObj.maxRange_m=4377.033691
    dbObj.probDetonate=0.850000
    dbObj.blastCharge_kg=323.832245
    dbObj.fragCharge_kg=279.111847
    dbObj.radCharge_kg=32.383224
    dbObj.fragMetal_kg=297.055908
    dbObj.fragFragment_kg=0.056261
    dbObj.fragSpread=0.300000
    return dbObj
