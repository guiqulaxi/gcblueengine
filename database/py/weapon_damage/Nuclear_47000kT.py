import pygcb
def CreateDBObject():
    dbObj=pygcb.tcWeaponDamage()
    dbObj.databaseClass='Nuclear-47000kT'
    dbObj.maxRange_m=100853.125000
    dbObj.probDetonate=0.900000
    dbObj.blastCharge_kg=51699998720.000000
    dbObj.fragCharge_kg=0.000000
    dbObj.radCharge_kg=23499999232.000000
    dbObj.fragMetal_kg=0.000000
    dbObj.fragFragment_kg=0.000000
    dbObj.fragSpread=1.000000
    return dbObj
