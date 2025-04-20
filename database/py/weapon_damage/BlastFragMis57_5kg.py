import pygcb
def CreateDBObject():
    dbObj=pygcb.tcWeaponDamage()
    dbObj.databaseClass='BlastFragMis57.5kg'
    dbObj.maxRange_m=3546.515137
    dbObj.probDetonate=0.850000
    dbObj.blastCharge_kg=11.504065
    dbObj.fragCharge_kg=25.680624
    dbObj.radCharge_kg=1.150406
    dbObj.fragMetal_kg=20.315311
    dbObj.fragFragment_kg=0.034259
    dbObj.fragSpread=0.300000
    return dbObj
