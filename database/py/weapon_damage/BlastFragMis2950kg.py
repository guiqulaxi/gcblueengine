import pygcb
def CreateDBObject():
    dbObj=pygcb.tcWeaponDamage()
    dbObj.databaseClass='BlastFragMis2950kg'
    dbObj.maxRange_m=10283.605469
    dbObj.probDetonate=0.850000
    dbObj.blastCharge_kg=303.711914
    dbObj.fragCharge_kg=1508.525391
    dbObj.radCharge_kg=30.371193
    dbObj.fragMetal_kg=1137.762695
    dbObj.fragFragment_kg=0.338217
    dbObj.fragSpread=0.300000
    return dbObj
