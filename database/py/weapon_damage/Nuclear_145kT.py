import pygcb
def CreateDBObject():
    dbObj=pygcb.tcWeaponDamage()
    dbObj.databaseClass='Nuclear-145kT'
    dbObj.maxRange_m=17802.064453
    dbObj.probDetonate=0.900000
    dbObj.blastCharge_kg=159500000.000000
    dbObj.fragCharge_kg=0.000000
    dbObj.radCharge_kg=72500000.000000
    dbObj.fragMetal_kg=0.000000
    dbObj.fragFragment_kg=0.000000
    dbObj.fragSpread=1.000000
    return dbObj
