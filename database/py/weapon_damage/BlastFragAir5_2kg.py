import pygcb
def CreateDBObject():
    dbObj=pygcb.tcWeaponDamage()
    dbObj.databaseClass='BlastFragAir5.2kg'
    dbObj.maxRange_m=1811.390259
    dbObj.probDetonate=0.850000
    dbObj.blastCharge_kg=1.348563
    dbObj.fragCharge_kg=2.116958
    dbObj.radCharge_kg=0.134856
    dbObj.fragMetal_kg=1.734479
    dbObj.fragFragment_kg=0.009081
    dbObj.fragSpread=0.070372
    return dbObj
