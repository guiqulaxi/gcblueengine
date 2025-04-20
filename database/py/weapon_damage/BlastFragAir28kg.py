import pygcb
def CreateDBObject():
    dbObj=pygcb.tcWeaponDamage()
    dbObj.databaseClass='BlastFragAir28kg'
    dbObj.maxRange_m=3096.988281
    dbObj.probDetonate=0.850000
    dbObj.blastCharge_kg=6.098897
    dbObj.fragCharge_kg=12.174069
    dbObj.radCharge_kg=0.609890
    dbObj.fragMetal_kg=9.727035
    dbObj.fragFragment_kg=0.026008
    dbObj.fragSpread=0.269823
    return dbObj
