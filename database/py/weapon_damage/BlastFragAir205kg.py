import pygcb
def CreateDBObject():
    dbObj=pygcb.tcWeaponDamage()
    dbObj.databaseClass='BlastFragAir205kg'
    dbObj.maxRange_m=4387.111816
    dbObj.probDetonate=0.850000
    dbObj.blastCharge_kg=34.587276
    dbObj.fragCharge_kg=95.841812
    dbObj.radCharge_kg=3.458728
    dbObj.fragMetal_kg=74.570908
    dbObj.fragFragment_kg=0.053189
    dbObj.fragSpread=0.300000
    return dbObj
