import pygcb
def CreateDBObject():
    dbObj=pygcb.tcWeaponDamage()
    dbObj.databaseClass='BlastFragAir52.5kg'
    dbObj.maxRange_m=3469.918701
    dbObj.probDetonate=0.850000
    dbObj.blastCharge_kg=10.621502
    dbObj.fragCharge_kg=23.368999
    dbObj.radCharge_kg=1.062150
    dbObj.fragMetal_kg=18.509499
    dbObj.fragFragment_kg=0.032760
    dbObj.fragSpread=0.300000
    return dbObj
