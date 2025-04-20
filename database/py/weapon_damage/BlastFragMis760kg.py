import pygcb
def CreateDBObject():
    dbObj=pygcb.tcWeaponDamage()
    dbObj.databaseClass='BlastFragMis760kg'
    dbObj.maxRange_m=6185.618652
    dbObj.probDetonate=0.850000
    dbObj.blastCharge_kg=103.665703
    dbObj.fragCharge_kg=371.689545
    dbObj.radCharge_kg=10.366570
    dbObj.fragMetal_kg=284.644775
    dbObj.fragFragment_kg=0.110456
    dbObj.fragSpread=0.300000
    return dbObj
