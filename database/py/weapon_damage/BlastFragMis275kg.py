import pygcb
def CreateDBObject():
    dbObj=pygcb.tcWeaponDamage()
    dbObj.databaseClass='BlastFragMis275kg'
    dbObj.maxRange_m=4632.565918
    dbObj.probDetonate=0.850000
    dbObj.blastCharge_kg=44.405178
    dbObj.fragCharge_kg=129.896545
    dbObj.radCharge_kg=4.440518
    dbObj.fragMetal_kg=100.698273
    dbObj.fragFragment_kg=0.059620
    dbObj.fragSpread=0.300000
    return dbObj
