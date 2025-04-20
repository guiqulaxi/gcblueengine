import pygcb
def CreateDBObject():
    dbObj=pygcb.tcWeaponDamage()
    dbObj.databaseClass='BlastFragMis3.5kg'
    dbObj.maxRange_m=1514.914917
    dbObj.probDetonate=0.850000
    dbObj.blastCharge_kg=0.941861
    dbObj.fragCharge_kg=1.402093
    dbObj.radCharge_kg=0.094186
    dbObj.fragMetal_kg=1.156046
    dbObj.fragFragment_kg=0.006495
    dbObj.fragSpread=0.061119
    return dbObj
