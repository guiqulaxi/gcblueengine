import pygcb
def CreateDBObject():
    dbObj=pygcb.tcWeaponDamage()
    dbObj.databaseClass='Nuclear-77.5kT'
    dbObj.maxRange_m=14751.986328
    dbObj.probDetonate=0.900000
    dbObj.blastCharge_kg=85250000.000000
    dbObj.fragCharge_kg=0.000000
    dbObj.radCharge_kg=38750000.000000
    dbObj.fragMetal_kg=0.000000
    dbObj.fragFragment_kg=0.000000
    dbObj.fragSpread=1.000000
    return dbObj
