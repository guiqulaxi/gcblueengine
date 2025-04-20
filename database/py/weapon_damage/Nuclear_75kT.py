import pygcb
def CreateDBObject():
    dbObj=pygcb.tcWeaponDamage()
    dbObj.databaseClass='Nuclear-75kT'
    dbObj.maxRange_m=14607.583008
    dbObj.probDetonate=0.900000
    dbObj.blastCharge_kg=82500000.000000
    dbObj.fragCharge_kg=0.000000
    dbObj.radCharge_kg=37500000.000000
    dbObj.fragMetal_kg=0.000000
    dbObj.fragFragment_kg=0.000000
    dbObj.fragSpread=1.000000
    return dbObj
