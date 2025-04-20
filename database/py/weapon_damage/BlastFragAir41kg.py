import pygcb
def CreateDBObject():
    dbObj=pygcb.tcWeaponDamage()
    dbObj.databaseClass='BlastFragAir41kg'
    dbObj.maxRange_m=3326.777100
    dbObj.probDetonate=0.850000
    dbObj.blastCharge_kg=8.544894
    dbObj.fragCharge_kg=18.083405
    dbObj.radCharge_kg=0.854489
    dbObj.fragMetal_kg=14.371702
    dbObj.fragFragment_kg=0.030066
    dbObj.fragSpread=0.300000
    return dbObj
