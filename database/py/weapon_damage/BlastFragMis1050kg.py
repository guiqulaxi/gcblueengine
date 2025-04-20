import pygcb
def CreateDBObject():
    dbObj=pygcb.tcWeaponDamage()
    dbObj.databaseClass='BlastFragMis1050kg'
    dbObj.maxRange_m=6833.807617
    dbObj.probDetonate=0.850000
    dbObj.blastCharge_kg=134.852005
    dbObj.fragCharge_kg=519.098694
    dbObj.radCharge_kg=13.485200
    dbObj.fragMetal_kg=396.049347
    dbObj.fragFragment_kg=0.137089
    dbObj.fragSpread=0.300000
    return dbObj
