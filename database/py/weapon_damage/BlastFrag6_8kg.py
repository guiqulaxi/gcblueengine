import pygcb
def CreateDBObject():
    dbObj=pygcb.tcWeaponDamage()
    dbObj.databaseClass='BlastFrag6.8kg'
    dbObj.maxRange_m=468.275238
    dbObj.probDetonate=0.850000
    dbObj.blastCharge_kg=2.400723
    dbObj.fragCharge_kg=2.139518
    dbObj.radCharge_kg=0.240072
    dbObj.fragMetal_kg=2.259759
    dbObj.fragFragment_kg=0.000981
    dbObj.fragSpread=0.300000
    return dbObj
