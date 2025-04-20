import pygcb
def CreateDBObject():
    dbObj=pygcb.tcWeaponDamage()
    dbObj.databaseClass='BlastFrag1.2kg'
    dbObj.maxRange_m=176.016418
    dbObj.probDetonate=0.850000
    dbObj.blastCharge_kg=0.427503
    dbObj.fragCharge_kg=0.374998
    dbObj.radCharge_kg=0.042750
    dbObj.fragMetal_kg=0.397499
    dbObj.fragFragment_kg=0.000287
    dbObj.fragSpread=0.300000
    return dbObj
