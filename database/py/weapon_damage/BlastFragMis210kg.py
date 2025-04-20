import pygcb
def CreateDBObject():
    dbObj=pygcb.tcWeaponDamage()
    dbObj.databaseClass='BlastFragMis210kg'
    dbObj.maxRange_m=4401.779297
    dbObj.probDetonate=0.850000
    dbObj.blastCharge_kg=35.306061
    dbObj.fragCharge_kg=98.262627
    dbObj.radCharge_kg=3.530606
    dbObj.fragMetal_kg=76.431313
    dbObj.fragFragment_kg=0.053561
    dbObj.fragSpread=0.300000
    return dbObj
