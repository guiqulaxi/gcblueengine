import pygcb
def CreateDBObject():
    dbObj=pygcb.tcWeaponDamage()
    dbObj.databaseClass='BlastFrag36kg'
    dbObj.maxRange_m=1054.652222
    dbObj.probDetonate=0.850000
    dbObj.blastCharge_kg=12.871619
    dbObj.fragCharge_kg=11.218921
    dbObj.radCharge_kg=1.287162
    dbObj.fragMetal_kg=11.909460
    dbObj.fragFragment_kg=0.003613
    dbObj.fragSpread=0.300000
    return dbObj
