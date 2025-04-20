import pygcb
def CreateDBObject():
    dbObj=pygcb.tcStoresDBObject()
    dbObj.mzClass='76mm/62 mk75 240 rounds'
    dbObj.natoClass='76mm/62 mk75 240 rounds'
    dbObj.mnModelType=0
    dbObj.mnType=0
    dbObj.cost=0.000000
    dbObj.weight_kg=0.000000
    dbObj.volume_m3=0.000000
    dbObj.initialYear=1900.000000
    dbObj.finalYear=2999.000000
    dbObj.country=''
    dbObj.designation=''
    dbObj.imageList=''
    dbObj.iconFileName=''
    dbObj.mz3DModelFileName=''
    dbObj.notes='I do not know the corerct number of rounds kept either in the gun or in the main magazine.  Navweaps says there is a single main feed drum that holds 70 rounds, a central screw hoist that holds 6 rounds, and a breech loading drum that holds 4 rounds.  there is no mention of main magazine storage much like there is for the 127mm/62 mark 45.  Given that they store 600 rounds per gun, and the OHP is a considerably smaller ship, im assuming 240 rounds.'
    dbObj.length_m=1.000000
    dbObj.width_m=1.000000
    dbObj.height_m=1.000000
    dbObj.displayName='240 rounds ammo mag'
    dbObj.capacity=240
    dbObj.maxVolume_m3=240.000000
    dbObj.maxWeight_kg=0.000000
    dbObj.moveTime=0.000000
    dbObj.compatibleItems=['76mm HE-MOM','76mm HE-SAPOM','76mm HE-SAPOMER']
    dbObj.CalculateParams()
    return dbObj
