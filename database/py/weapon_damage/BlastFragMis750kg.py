import pygcb
def CreateDBObject():
    dbObj=pygcb.tcWeaponDamage()
    dbObj.databaseClass='BlastFragMis750kg'
    dbObj.maxRange_m=6161.369629
    dbObj.probDetonate=0.850000
    dbObj.blastCharge_kg=102.546677
    dbObj.fragCharge_kg=366.635559
    dbObj.radCharge_kg=10.254668
    dbObj.fragMetal_kg=280.817780
    dbObj.fragFragment_kg=0.109523
    dbObj.fragSpread=0.300000
    return dbObj
