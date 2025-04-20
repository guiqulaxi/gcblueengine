import pygcb
def CreateDBObject():
    dbObj=pygcb.tcWeaponDamage()
    dbObj.databaseClass='BlastFragMis44kg'
    dbObj.maxRange_m=3365.101318
    dbObj.probDetonate=0.850000
    dbObj.blastCharge_kg=9.093497
    dbObj.fragCharge_kg=19.457668
    dbObj.radCharge_kg=0.909350
    dbObj.fragMetal_kg=15.448834
    dbObj.fragFragment_kg=0.030775
    dbObj.fragSpread=0.300000
    return dbObj
