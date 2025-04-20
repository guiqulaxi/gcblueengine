import pygcb
def CreateDBObject():
    dbObj=pygcb.tcWeaponDamage()
    dbObj.databaseClass='BlastFragAir3200kg'
    dbObj.maxRange_m=10583.812500
    dbObj.probDetonate=0.850000
    dbObj.blastCharge_kg=323.030273
    dbObj.fragCharge_kg=1640.646484
    dbObj.radCharge_kg=32.303028
    dbObj.fragMetal_kg=1236.323242
    dbObj.fragFragment_kg=0.360760
    dbObj.fragSpread=0.300000
    return dbObj
