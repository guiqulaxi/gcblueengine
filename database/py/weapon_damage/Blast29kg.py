import pygcb
def CreateDBObject():
    dbObj=pygcb.tcWeaponDamage()
    dbObj.databaseClass='Blast29kg'
    dbObj.maxRange_m=38.396320
    dbObj.probDetonate=0.850000
    dbObj.blastCharge_kg=29.000000
    dbObj.fragCharge_kg=0.000000
    dbObj.radCharge_kg=2.900000
    dbObj.fragMetal_kg=0.000000
    dbObj.fragFragment_kg=0.000000
    dbObj.fragSpread=0.000000
    return dbObj
