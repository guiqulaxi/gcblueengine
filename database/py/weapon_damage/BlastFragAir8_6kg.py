import pygcb
def CreateDBObject():
    dbObj=pygcb.tcWeaponDamage()
    dbObj.databaseClass='BlastFragAir8.6kg'
    dbObj.maxRange_m=2210.769287
    dbObj.probDetonate=0.850000
    dbObj.blastCharge_kg=2.123607
    dbObj.fragCharge_kg=3.572262
    dbObj.radCharge_kg=0.212361
    dbObj.fragMetal_kg=2.904131
    dbObj.fragFragment_kg=0.013322
    dbObj.fragSpread=0.091674
    return dbObj
