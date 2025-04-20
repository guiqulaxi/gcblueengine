import pygcb
def CreateDBObject():
    dbObj=pygcb.tcWeaponDamage()
    dbObj.databaseClass='BlastFrag2250kg'
    dbObj.maxRange_m=6296.739258
    dbObj.probDetonate=0.850000
    dbObj.blastCharge_kg=809.809631
    dbObj.fragCharge_kg=697.626892
    dbObj.radCharge_kg=80.980965
    dbObj.fragMetal_kg=742.563477
    dbObj.fragFragment_kg=0.121812
    dbObj.fragSpread=0.300000
    return dbObj
