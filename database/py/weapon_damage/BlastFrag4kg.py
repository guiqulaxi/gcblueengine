import pygcb
def CreateDBObject():
    dbObj=pygcb.tcWeaponDamage()
    dbObj.databaseClass='BlastFrag4kg'
    dbObj.maxRange_m=355.480072
    dbObj.probDetonate=0.850000
    dbObj.blastCharge_kg=1.405810
    dbObj.fragCharge_kg=1.262794
    dbObj.radCharge_kg=0.140581
    dbObj.fragMetal_kg=1.331397
    dbObj.fragFragment_kg=0.000666
    dbObj.fragSpread=0.300000
    return dbObj
