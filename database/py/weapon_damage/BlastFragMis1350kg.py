import pygcb
def CreateDBObject():
    dbObj=pygcb.tcWeaponDamage()
    dbObj.databaseClass='BlastFragMis1350kg'
    dbObj.maxRange_m=7595.896484
    dbObj.probDetonate=0.850000
    dbObj.blastCharge_kg=165.013611
    dbObj.fragCharge_kg=672.990906
    dbObj.radCharge_kg=16.501360
    dbObj.fragMetal_kg=511.995453
    dbObj.fragFragment_kg=0.172738
    dbObj.fragSpread=0.300000
    return dbObj
