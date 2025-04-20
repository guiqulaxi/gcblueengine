import pygcb
def CreateDBObject():
    dbObj=pygcb.tcWeaponDamage()
    dbObj.databaseClass='BlastFragMis215kg'
    dbObj.maxRange_m=4415.915527
    dbObj.probDetonate=0.850000
    dbObj.blastCharge_kg=36.021912
    dbObj.fragCharge_kg=100.685394
    dbObj.radCharge_kg=3.602191
    dbObj.fragMetal_kg=78.292694
    dbObj.fragFragment_kg=0.053921
    dbObj.fragSpread=0.300000
    return dbObj
