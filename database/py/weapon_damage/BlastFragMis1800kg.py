import pygcb
def CreateDBObject():
    dbObj=pygcb.tcWeaponDamage()
    dbObj.databaseClass='BlastFragMis1800kg'
    dbObj.maxRange_m=8533.395508
    dbObj.probDetonate=0.850000
    dbObj.blastCharge_kg=207.246948
    dbObj.fragCharge_kg=905.835388
    dbObj.radCharge_kg=20.724693
    dbObj.fragMetal_kg=686.917664
    dbObj.fragFragment_kg=0.223243
    dbObj.fragSpread=0.300000
    return dbObj
