import pygcb
def CreateDBObject():
    dbObj=pygcb.tcWeaponDamage()
    dbObj.databaseClass='BlastFrag140kg'
    dbObj.maxRange_m=1998.250977
    dbObj.probDetonate=0.850000
    dbObj.blastCharge_kg=50.278126
    dbObj.fragCharge_kg=43.481251
    dbObj.radCharge_kg=5.027812
    dbObj.fragMetal_kg=46.240623
    dbObj.fragFragment_kg=0.011653
    dbObj.fragSpread=0.300000
    return dbObj
