# -*- coding: utf-8 -*-
import pygcb
def CreateDBObject():
    dbObj=pygcb.tcDamageEffect()
    dbObj.databaseClass='PC Class Cormoran durability'
    dbObj.blastEffect=[pygcb.DamagePoint()]*13
    dbObj.blastEffect[0].effectLevel=0.000000
    dbObj.blastEffect[0].damageFactor=0.000000
    dbObj.blastEffect[1].effectLevel=2.880000
    dbObj.blastEffect[1].damageFactor=0.000000
    dbObj.blastEffect[2].effectLevel=2.980000
    dbObj.blastEffect[2].damageFactor=0.100000
    dbObj.blastEffect[3].effectLevel=3.280000
    dbObj.blastEffect[3].damageFactor=0.200000
    dbObj.blastEffect[4].effectLevel=3.780000
    dbObj.blastEffect[4].damageFactor=0.300000
    dbObj.blastEffect[5].effectLevel=4.490000
    dbObj.blastEffect[5].damageFactor=0.400000
    dbObj.blastEffect[6].effectLevel=5.390000
    dbObj.blastEffect[6].damageFactor=0.500000
    dbObj.blastEffect[7].effectLevel=6.500000
    dbObj.blastEffect[7].damageFactor=0.600000
    dbObj.blastEffect[8].effectLevel=7.810000
    dbObj.blastEffect[8].damageFactor=0.700000
    dbObj.blastEffect[9].effectLevel=9.320000
    dbObj.blastEffect[9].damageFactor=0.800000
    dbObj.blastEffect[10].effectLevel=11.030000
    dbObj.blastEffect[10].damageFactor=0.900000
    dbObj.blastEffect[11].effectLevel=12.940000
    dbObj.blastEffect[11].damageFactor=1.000000
    dbObj.blastEffect[12].effectLevel=16.299999
    dbObj.blastEffect[12].damageFactor=2.000000
    dbObj.waterBlastEffect=[pygcb.DamagePoint()]*26
    dbObj.waterBlastEffect[0].effectLevel=0.000000
    dbObj.waterBlastEffect[0].damageFactor=0.000000
    dbObj.waterBlastEffect[1].effectLevel=66.997002
    dbObj.waterBlastEffect[1].damageFactor=0.043000
    dbObj.waterBlastEffect[2].effectLevel=76.111000
    dbObj.waterBlastEffect[2].damageFactor=0.045000
    dbObj.waterBlastEffect[3].effectLevel=86.420998
    dbObj.waterBlastEffect[3].damageFactor=0.048000
    dbObj.waterBlastEffect[4].effectLevel=98.079002
    dbObj.waterBlastEffect[4].damageFactor=0.050000
    dbObj.waterBlastEffect[5].effectLevel=111.258003
    dbObj.waterBlastEffect[5].damageFactor=0.053000
    dbObj.waterBlastEffect[6].effectLevel=126.150002
    dbObj.waterBlastEffect[6].damageFactor=0.056000
    dbObj.waterBlastEffect[7].effectLevel=142.975006
    dbObj.waterBlastEffect[7].damageFactor=0.059000
    dbObj.waterBlastEffect[8].effectLevel=161.983994
    dbObj.waterBlastEffect[8].damageFactor=0.062000
    dbObj.waterBlastEffect[9].effectLevel=183.462997
    dbObj.waterBlastEffect[9].damageFactor=0.067000
    dbObj.waterBlastEffect[10].effectLevel=207.738998
    dbObj.waterBlastEffect[10].damageFactor=0.071000
    dbObj.waterBlastEffect[11].effectLevel=235.195999
    dbObj.waterBlastEffect[11].damageFactor=0.077000
    dbObj.waterBlastEffect[12].effectLevel=266.282013
    dbObj.waterBlastEffect[12].damageFactor=0.083000
    dbObj.waterBlastEffect[13].effectLevel=301.536987
    dbObj.waterBlastEffect[13].damageFactor=0.091000
    dbObj.waterBlastEffect[14].effectLevel=341.614990
    dbObj.waterBlastEffect[14].damageFactor=0.100000
    dbObj.waterBlastEffect[15].effectLevel=387.341003
    dbObj.waterBlastEffect[15].damageFactor=0.111000
    dbObj.waterBlastEffect[16].effectLevel=439.786987
    dbObj.waterBlastEffect[16].damageFactor=0.125000
    dbObj.waterBlastEffect[17].effectLevel=500.412994
    dbObj.waterBlastEffect[17].damageFactor=0.143000
    dbObj.waterBlastEffect[18].effectLevel=571.330017
    dbObj.waterBlastEffect[18].damageFactor=0.167000
    dbObj.waterBlastEffect[19].effectLevel=655.831970
    dbObj.waterBlastEffect[19].damageFactor=0.200000
    dbObj.waterBlastEffect[20].effectLevel=759.603027
    dbObj.waterBlastEffect[20].damageFactor=0.250000
    dbObj.waterBlastEffect[21].effectLevel=893.932007
    dbObj.waterBlastEffect[21].damageFactor=0.333000
    dbObj.waterBlastEffect[22].effectLevel=1086.647949
    dbObj.waterBlastEffect[22].damageFactor=0.500000
    dbObj.waterBlastEffect[23].effectLevel=1441.629028
    dbObj.waterBlastEffect[23].damageFactor=1.000000
    dbObj.waterBlastEffect[24].effectLevel=1859.266968
    dbObj.waterBlastEffect[24].damageFactor=2.000000
    dbObj.waterBlastEffect[25].effectLevel=2375.405029
    dbObj.waterBlastEffect[25].damageFactor=4.000000
    dbObj.fragEffect=[pygcb.DamagePoint()]*20
    dbObj.fragEffect[0].effectLevel=0.000000
    dbObj.fragEffect[0].damageFactor=0.000000
    dbObj.fragEffect[1].effectLevel=120734.539062
    dbObj.fragEffect[1].damageFactor=0.000000
    dbObj.fragEffect[2].effectLevel=300000.000000
    dbObj.fragEffect[2].damageFactor=0.021990
    dbObj.fragEffect[3].effectLevel=600000.000000
    dbObj.fragEffect[3].damageFactor=0.031100
    dbObj.fragEffect[4].effectLevel=1000000.000000
    dbObj.fragEffect[4].damageFactor=0.040150
    dbObj.fragEffect[5].effectLevel=3000000.000000
    dbObj.fragEffect[5].damageFactor=0.069540
    dbObj.fragEffect[6].effectLevel=6000000.000000
    dbObj.fragEffect[6].damageFactor=0.098340
    dbObj.fragEffect[7].effectLevel=10000000.000000
    dbObj.fragEffect[7].damageFactor=0.126950
    dbObj.fragEffect[8].effectLevel=30000000.000000
    dbObj.fragEffect[8].damageFactor=0.219890
    dbObj.fragEffect[9].effectLevel=60000000.000000
    dbObj.fragEffect[9].damageFactor=0.310970
    dbObj.fragEffect[10].effectLevel=100000000.000000
    dbObj.fragEffect[10].damageFactor=0.401460
    dbObj.fragEffect[11].effectLevel=300000000.000000
    dbObj.fragEffect[11].damageFactor=0.695360
    dbObj.fragEffect[12].effectLevel=600000000.000000
    dbObj.fragEffect[12].damageFactor=0.983380
    dbObj.fragEffect[13].effectLevel=1000000000.000000
    dbObj.fragEffect[13].damageFactor=1.269540
    dbObj.fragEffect[14].effectLevel=3000000000.000000
    dbObj.fragEffect[14].damageFactor=2.198910
    dbObj.fragEffect[15].effectLevel=6000000000.000000
    dbObj.fragEffect[15].damageFactor=3.109730
    dbObj.fragEffect[16].effectLevel=10000000000.000000
    dbObj.fragEffect[16].damageFactor=4.014640
    dbObj.fragEffect[17].effectLevel=30000001024.000000
    dbObj.fragEffect[17].damageFactor=6.953570
    dbObj.fragEffect[18].effectLevel=60000002048.000000
    dbObj.fragEffect[18].damageFactor=9.833830
    dbObj.fragEffect[19].effectLevel=99999997952.000000
    dbObj.fragEffect[19].damageFactor=12.695420
    dbObj.radEffect=[pygcb.DamagePoint()]*6
    dbObj.radEffect[0].effectLevel=0.000000
    dbObj.radEffect[0].damageFactor=0.000000
    dbObj.radEffect[1].effectLevel=5000.000000
    dbObj.radEffect[1].damageFactor=0.000000
    dbObj.radEffect[2].effectLevel=25000.000000
    dbObj.radEffect[2].damageFactor=0.400000
    dbObj.radEffect[3].effectLevel=50000.000000
    dbObj.radEffect[3].damageFactor=2.000000
    dbObj.radEffect[4].effectLevel=125000.000000
    dbObj.radEffect[4].damageFactor=5.000000
    dbObj.radEffect[5].effectLevel=250000.000000
    dbObj.radEffect[5].damageFactor=20.000000
    dbObj.internalEffect=[pygcb.DamagePoint()]*11
    dbObj.internalEffect[0].effectLevel=0.000000
    dbObj.internalEffect[0].damageFactor=0.000000
    dbObj.internalEffect[1].effectLevel=1.000000
    dbObj.internalEffect[1].damageFactor=0.036460
    dbObj.internalEffect[2].effectLevel=2.000000
    dbObj.internalEffect[2].damageFactor=0.072960
    dbObj.internalEffect[3].effectLevel=4.000000
    dbObj.internalEffect[3].damageFactor=0.145880
    dbObj.internalEffect[4].effectLevel=8.000000
    dbObj.internalEffect[4].damageFactor=0.291790
    dbObj.internalEffect[5].effectLevel=16.000000
    dbObj.internalEffect[5].damageFactor=0.583460
    dbObj.internalEffect[6].effectLevel=32.000000
    dbObj.internalEffect[6].damageFactor=1.167050
    dbObj.internalEffect[7].effectLevel=64.000000
    dbObj.internalEffect[7].damageFactor=2.334310
    dbObj.internalEffect[8].effectLevel=128.000000
    dbObj.internalEffect[8].damageFactor=4.668620
    dbObj.internalEffect[9].effectLevel=256.000000
    dbObj.internalEffect[9].damageFactor=9.336410
    dbObj.internalEffect[10].effectLevel=512.000000
    dbObj.internalEffect[10].damageFactor=18.674490
    return dbObj
