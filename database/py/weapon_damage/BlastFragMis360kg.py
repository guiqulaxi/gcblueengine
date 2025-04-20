import pygcb
def CreateDBObject():
    dbObj=pygcb.tcWeaponDamage()
    dbObj.databaseClass='BlastFragMis360kg'
    dbObj.maxRange_m=4988.940430
    dbObj.probDetonate=0.850000
    dbObj.blastCharge_kg=55.739094
    dbObj.fragCharge_kg=171.640610
    dbObj.radCharge_kg=5.573909
    dbObj.fragMetal_kg=132.620300
    dbObj.fragFragment_kg=0.069727
    dbObj.fragSpread=0.300000
    return dbObj
