import pygcb
def CreateDBObject():
    dbObj=pygcb.tcWeaponDamage()
    dbObj.databaseClass='BlastFrag44kg'
    dbObj.maxRange_m=1156.804688
    dbObj.probDetonate=0.850000
    dbObj.blastCharge_kg=15.746671
    dbObj.fragCharge_kg=13.702220
    dbObj.radCharge_kg=1.574667
    dbObj.fragMetal_kg=14.551110
    dbObj.fragFragment_kg=0.004250
    dbObj.fragSpread=0.300000
    return dbObj
