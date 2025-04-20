import pygcb
def CreateDBObject():
    dbObj=pygcb.tcWeaponDamage()
    dbObj.databaseClass='BlastFragMis36kg'
    dbObj.maxRange_m=3252.695801
    dbObj.probDetonate=0.850000
    dbObj.blastCharge_kg=7.618304
    dbObj.fragCharge_kg=15.801131
    dbObj.radCharge_kg=0.761830
    dbObj.fragMetal_kg=12.580565
    dbObj.fragFragment_kg=0.028723
    dbObj.fragSpread=0.300000
    return dbObj
