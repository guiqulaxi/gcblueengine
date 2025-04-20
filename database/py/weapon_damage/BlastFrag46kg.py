import pygcb
def CreateDBObject():
    dbObj=pygcb.tcWeaponDamage()
    dbObj.databaseClass='BlastFrag46kg'
    dbObj.maxRange_m=1179.938721
    dbObj.probDetonate=0.850000
    dbObj.blastCharge_kg=16.465574
    dbObj.fragCharge_kg=14.322950
    dbObj.radCharge_kg=1.646557
    dbObj.fragMetal_kg=15.211475
    dbObj.fragFragment_kg=0.004401
    dbObj.fragSpread=0.300000
    return dbObj
