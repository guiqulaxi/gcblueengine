import pygcb
def CreateDBObject():
    dbObj=pygcb.tcWeaponDamage()
    dbObj.databaseClass='Nuclear-19000kT'
    dbObj.maxRange_m=76857.468750
    dbObj.probDetonate=0.900000
    dbObj.blastCharge_kg=20899999744.000000
    dbObj.fragCharge_kg=0.000000
    dbObj.radCharge_kg=9500000256.000000
    dbObj.fragMetal_kg=0.000000
    dbObj.fragFragment_kg=0.000000
    dbObj.fragSpread=1.000000
    return dbObj
