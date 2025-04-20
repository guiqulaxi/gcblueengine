import pygcb
def CreateDBObject():
    dbObj=pygcb.tcWeaponDamage()
    dbObj.databaseClass='BlastFragMis3.7kg'
    dbObj.maxRange_m=1557.414307
    dbObj.probDetonate=0.850000
    dbObj.blastCharge_kg=0.990610
    dbObj.fragCharge_kg=1.485593
    dbObj.radCharge_kg=0.099061
    dbObj.fragMetal_kg=1.223796
    dbObj.fragFragment_kg=0.006837
    dbObj.fragSpread=0.061807
    return dbObj
