import pygcb
def CreateDBObject():
    dbObj=pygcb.tcWeaponDamage()
    dbObj.databaseClass='Blast650kg'
    dbObj.maxRange_m=108.146187
    dbObj.probDetonate=0.850000
    dbObj.blastCharge_kg=650.000000
    dbObj.fragCharge_kg=0.000000
    dbObj.radCharge_kg=65.000000
    dbObj.fragMetal_kg=0.000000
    dbObj.fragFragment_kg=0.000000
    dbObj.fragSpread=0.000000
    return dbObj
