import pygcb
def CreateDBObject():
    dbObj=pygcb.tcWeaponDamage()
    dbObj.databaseClass='BlastFrag30kg'
    dbObj.maxRange_m=965.568787
    dbObj.probDetonate=0.850000
    dbObj.blastCharge_kg=10.716116
    dbObj.fragCharge_kg=9.355923
    dbObj.radCharge_kg=1.071612
    dbObj.fragMetal_kg=9.927961
    dbObj.fragFragment_kg=0.003102
    dbObj.fragSpread=0.300000
    return dbObj
