import pygcb
def CreateDBObject():
    dbObj=pygcb.tcWeaponDamage()
    dbObj.databaseClass='BlastFragAir1550kg'
    dbObj.maxRange_m=8037.991699
    dbObj.probDetonate=0.850000
    dbObj.blastCharge_kg=184.178894
    dbObj.fragCharge_kg=776.214050
    dbObj.radCharge_kg=18.417891
    dbObj.fragMetal_kg=589.607056
    dbObj.fragFragment_kg=0.195623
    dbObj.fragSpread=0.300000
    return dbObj
