import pygcb
def CreateDBObject():
    dbObj=pygcb.tcWeaponDamage()
    dbObj.databaseClass='BlastFragAir2750kg'
    dbObj.maxRange_m=10026.281250
    dbObj.probDetonate=0.850000
    dbObj.blastCharge_kg=287.882782
    dbObj.fragCharge_kg=1403.078125
    dbObj.radCharge_kg=28.788277
    dbObj.fragMetal_kg=1059.039062
    dbObj.fragFragment_kg=0.319565
    dbObj.fragSpread=0.300000
    return dbObj
