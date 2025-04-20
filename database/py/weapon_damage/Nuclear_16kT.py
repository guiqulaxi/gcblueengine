import pygcb
def CreateDBObject():
    dbObj=pygcb.tcWeaponDamage()
    dbObj.databaseClass='Nuclear-16kT'
    dbObj.maxRange_m=9189.586914
    dbObj.probDetonate=0.900000
    dbObj.blastCharge_kg=17600000.000000
    dbObj.fragCharge_kg=0.000000
    dbObj.radCharge_kg=8000000.000000
    dbObj.fragMetal_kg=0.000000
    dbObj.fragFragment_kg=0.000000
    dbObj.fragSpread=1.000000
    return dbObj
