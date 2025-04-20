import pygcb
def CreateDBObject():
    dbObj=pygcb.tcWeaponDamage()
    dbObj.databaseClass='BlastFragAir225kg'
    dbObj.maxRange_m=4442.708008
    dbObj.probDetonate=0.850000
    dbObj.blastCharge_kg=37.445068
    dbObj.fragCharge_kg=105.536621
    dbObj.radCharge_kg=3.744507
    dbObj.fragMetal_kg=82.018311
    dbObj.fragFragment_kg=0.054606
    dbObj.fragSpread=0.300000
    return dbObj
