import pygcb
def CreateDBObject():
    dbObj=pygcb.tcWeaponDamage()
    dbObj.databaseClass='Nuclear-31000kT'
    dbObj.maxRange_m=89016.085938
    dbObj.probDetonate=0.900000
    dbObj.blastCharge_kg=34100000768.000000
    dbObj.fragCharge_kg=0.000000
    dbObj.radCharge_kg=15500000256.000000
    dbObj.fragMetal_kg=0.000000
    dbObj.fragFragment_kg=0.000000
    dbObj.fragSpread=1.000000
    return dbObj
