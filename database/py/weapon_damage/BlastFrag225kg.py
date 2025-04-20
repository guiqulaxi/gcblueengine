import pygcb
def CreateDBObject():
    dbObj=pygcb.tcWeaponDamage()
    dbObj.databaseClass='BlastFrag225kg'
    dbObj.maxRange_m=2464.865723
    dbObj.probDetonate=0.850000
    dbObj.blastCharge_kg=80.866425
    dbObj.fragCharge_kg=69.839050
    dbObj.radCharge_kg=8.086642
    dbObj.fragMetal_kg=74.294525
    dbObj.fragFragment_kg=0.017522
    dbObj.fragSpread=0.300000
    return dbObj
