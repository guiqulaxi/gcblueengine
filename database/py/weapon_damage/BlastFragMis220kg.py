import pygcb
def CreateDBObject():
    dbObj=pygcb.tcWeaponDamage()
    dbObj.databaseClass='BlastFragMis220kg'
    dbObj.maxRange_m=4429.549316
    dbObj.probDetonate=0.850000
    dbObj.blastCharge_kg=36.734890
    dbObj.fragCharge_kg=103.110069
    dbObj.radCharge_kg=3.673489
    dbObj.fragMetal_kg=80.155037
    dbObj.fragFragment_kg=0.054269
    dbObj.fragSpread=0.300000
    return dbObj
