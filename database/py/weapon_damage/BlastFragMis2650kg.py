import pygcb
def CreateDBObject():
    dbObj=pygcb.tcWeaponDamage()
    dbObj.databaseClass='BlastFragMis2650kg'
    dbObj.maxRange_m=9891.492188
    dbObj.probDetonate=0.850000
    dbObj.blastCharge_kg=279.835205
    dbObj.fragCharge_kg=1350.443237
    dbObj.radCharge_kg=27.983522
    dbObj.fragMetal_kg=1019.721619
    dbObj.fragFragment_kg=0.310040
    dbObj.fragSpread=0.300000
    return dbObj
