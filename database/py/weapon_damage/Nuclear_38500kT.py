import pygcb
def CreateDBObject():
    dbObj=pygcb.tcWeaponDamage()
    dbObj.databaseClass='Nuclear-38500kT'
    dbObj.maxRange_m=94994.445312
    dbObj.probDetonate=0.900000
    dbObj.blastCharge_kg=42349998080.000000
    dbObj.fragCharge_kg=0.000000
    dbObj.radCharge_kg=19249999872.000000
    dbObj.fragMetal_kg=0.000000
    dbObj.fragFragment_kg=0.000000
    dbObj.fragSpread=1.000000
    return dbObj
