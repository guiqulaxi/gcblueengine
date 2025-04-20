import pygcb
def CreateDBObject():
    dbObj=pygcb.tcLauncherDBObject()
    dbObj.mzClass='Harrier GR.7 3-7'
    dbObj.natoClass=''
    dbObj.mnModelType=0
    dbObj.mnType=0
    dbObj.cost=0.000000
    dbObj.weight_kg=0.000000
    dbObj.volume_m3=0.000000
    dbObj.initialYear=0.000000
    dbObj.finalYear=2999.000000
    dbObj.country=''
    dbObj.designation=''
    dbObj.imageList=''
    dbObj.iconFileName=''
    dbObj.mz3DModelFileName=''
    dbObj.notes=''
    dbObj.length_m=0.000000
    dbObj.width_m=0.000000
    dbObj.height_m=0.000000
    dbObj.childClassList=['100 gallon wing tank','190 gallon wing tank','300 gallon wing tank','68mm SNEB Rockets','AGM-65D','GBU-1/B','GBU-12/B','GBU-16/B','M117','Mk-81','Mk-82','Mk-83']
    dbObj.childCapacityList=[2,2,2,36,2,4,6,4,2,4,4,2]
    dbObj.childLoadTime_s=[240.000000,240.000000,240.000000,240.000000,360.000000,360.000000,480.000000,360.000000,240.000000,360.000000,360.000000,240.000000]
    dbObj.childCycleTime_s=[1.000000,1.000000,1.000000,0.100000,1.000000,1.000000,1.000000,1.000000,0.200000,0.200000,0.200000,0.200000]
    dbObj.CalculateParams()
    return dbObj
