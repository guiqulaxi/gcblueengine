import pygcb
def CreateDBObject():
    dbObj=pygcb.tcWeaponDamage()
    dbObj.databaseClass='BlastFrag5.2kg'
    dbObj.maxRange_m=404.326874
    dbObj.probDetonate=0.850000
    dbObj.blastCharge_kg=1.831339
    dbObj.fragCharge_kg=1.639107
    dbObj.radCharge_kg=0.183134
    dbObj.fragMetal_kg=1.729554
    dbObj.fragFragment_kg=0.000795
    dbObj.fragSpread=0.300000
    return dbObj
