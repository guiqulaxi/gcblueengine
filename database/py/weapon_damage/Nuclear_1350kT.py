import pygcb
def CreateDBObject():
    dbObj=pygcb.tcWeaponDamage()
    dbObj.databaseClass='Nuclear-1350kT'
    dbObj.maxRange_m=34766.433594
    dbObj.probDetonate=0.900000
    dbObj.blastCharge_kg=1484999936.000000
    dbObj.fragCharge_kg=0.000000
    dbObj.radCharge_kg=675000000.000000
    dbObj.fragMetal_kg=0.000000
    dbObj.fragFragment_kg=0.000000
    dbObj.fragSpread=1.000000
    return dbObj
