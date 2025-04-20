import pygcb
def CreateDBObject():
    dbObj=pygcb.tcWeaponDamage()
    dbObj.databaseClass='BlastFragMis100kg'
    dbObj.maxRange_m=3861.730225
    dbObj.probDetonate=0.850000
    dbObj.blastCharge_kg=18.642252
    dbObj.fragCharge_kg=45.571831
    dbObj.radCharge_kg=1.864225
    dbObj.fragMetal_kg=35.785915
    dbObj.fragFragment_kg=0.040805
    dbObj.fragSpread=0.300000
    return dbObj
