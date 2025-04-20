import pygcb
def CreateDBObject():
    dbObj=pygcb.tcWeaponDamage()
    dbObj.databaseClass='Pen215kg'
    dbObj.maxRange_m=66.440170
    dbObj.probDetonate=0.850000
    dbObj.blastCharge_kg=150.500000
    dbObj.fragCharge_kg=0.000000
    dbObj.radCharge_kg=21.500000
    dbObj.fragMetal_kg=0.000000
    dbObj.fragFragment_kg=0.000000
    dbObj.fragSpread=0.000000
    return dbObj
