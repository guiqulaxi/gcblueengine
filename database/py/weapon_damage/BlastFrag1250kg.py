import pygcb
def CreateDBObject():
    dbObj=pygcb.tcWeaponDamage()
    dbObj.databaseClass='BlastFrag1250kg'
    dbObj.maxRange_m=5002.972656
    dbObj.probDetonate=0.850000
    dbObj.blastCharge_kg=449.824127
    dbObj.fragCharge_kg=387.617249
    dbObj.radCharge_kg=44.982414
    dbObj.fragMetal_kg=412.558624
    dbObj.fragFragment_kg=0.074523
    dbObj.fragSpread=0.300000
    return dbObj
