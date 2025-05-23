# -*- coding: utf-8 -*-
import pygcb
def CreateDBObject():
    dbObj=pygcb.tcDamageEffect()
    dbObj.databaseClass='Avenger MCM durability'
    dbObj.blastEffect=[pygcb.DamagePoint()]*13
    dbObj.blastEffect[0].effectLevel=0.000000
    dbObj.blastEffect[0].damageFactor=0.000000
    dbObj.blastEffect[1].effectLevel=2.110000
    dbObj.blastEffect[1].damageFactor=0.000000
    dbObj.blastEffect[2].effectLevel=2.220000
    dbObj.blastEffect[2].damageFactor=0.100000
    dbObj.blastEffect[3].effectLevel=2.520000
    dbObj.blastEffect[3].damageFactor=0.200000
    dbObj.blastEffect[4].effectLevel=3.020000
    dbObj.blastEffect[4].damageFactor=0.300000
    dbObj.blastEffect[5].effectLevel=3.730000
    dbObj.blastEffect[5].damageFactor=0.400000
    dbObj.blastEffect[6].effectLevel=4.640000
    dbObj.blastEffect[6].damageFactor=0.500000
    dbObj.blastEffect[7].effectLevel=5.750000
    dbObj.blastEffect[7].damageFactor=0.600000
    dbObj.blastEffect[8].effectLevel=7.060000
    dbObj.blastEffect[8].damageFactor=0.700000
    dbObj.blastEffect[9].effectLevel=8.580000
    dbObj.blastEffect[9].damageFactor=0.800000
    dbObj.blastEffect[10].effectLevel=10.300000
    dbObj.blastEffect[10].damageFactor=0.900000
    dbObj.blastEffect[11].effectLevel=12.220000
    dbObj.blastEffect[11].damageFactor=1.000000
    dbObj.blastEffect[12].effectLevel=15.390000
    dbObj.blastEffect[12].damageFactor=2.000000
    dbObj.waterBlastEffect=[pygcb.DamagePoint()]*28
    dbObj.waterBlastEffect[0].effectLevel=0.000000
    dbObj.waterBlastEffect[0].damageFactor=0.000000
    dbObj.waterBlastEffect[1].effectLevel=64.749001
    dbObj.waterBlastEffect[1].damageFactor=0.040000
    dbObj.waterBlastEffect[2].effectLevel=73.633003
    dbObj.waterBlastEffect[2].damageFactor=0.042000
    dbObj.waterBlastEffect[3].effectLevel=83.693001
    dbObj.waterBlastEffect[3].damageFactor=0.043000
    dbObj.waterBlastEffect[4].effectLevel=95.078003
    dbObj.waterBlastEffect[4].damageFactor=0.045000
    dbObj.waterBlastEffect[5].effectLevel=107.958000
    dbObj.waterBlastEffect[5].damageFactor=0.048000
    dbObj.waterBlastEffect[6].effectLevel=122.521004
    dbObj.waterBlastEffect[6].damageFactor=0.050000
    dbObj.waterBlastEffect[7].effectLevel=138.983994
    dbObj.waterBlastEffect[7].damageFactor=0.053000
    dbObj.waterBlastEffect[8].effectLevel=157.587006
    dbObj.waterBlastEffect[8].damageFactor=0.056000
    dbObj.waterBlastEffect[9].effectLevel=178.606003
    dbObj.waterBlastEffect[9].damageFactor=0.059000
    dbObj.waterBlastEffect[10].effectLevel=202.352005
    dbObj.waterBlastEffect[10].damageFactor=0.062000
    dbObj.waterBlastEffect[11].effectLevel=229.182999
    dbObj.waterBlastEffect[11].damageFactor=0.067000
    dbObj.waterBlastEffect[12].effectLevel=259.509003
    dbObj.waterBlastEffect[12].damageFactor=0.071000
    dbObj.waterBlastEffect[13].effectLevel=293.808014
    dbObj.waterBlastEffect[13].damageFactor=0.077000
    dbObj.waterBlastEffect[14].effectLevel=332.641998
    dbObj.waterBlastEffect[14].damageFactor=0.083000
    dbObj.waterBlastEffect[15].effectLevel=376.682007
    dbObj.waterBlastEffect[15].damageFactor=0.091000
    dbObj.waterBlastEffect[16].effectLevel=426.747986
    dbObj.waterBlastEffect[16].damageFactor=0.100000
    dbObj.waterBlastEffect[17].effectLevel=483.868988
    dbObj.waterBlastEffect[17].damageFactor=0.111000
    dbObj.waterBlastEffect[18].effectLevel=549.385010
    dbObj.waterBlastEffect[18].damageFactor=0.125000
    dbObj.waterBlastEffect[19].effectLevel=625.119019
    dbObj.waterBlastEffect[19].damageFactor=0.143000
    dbObj.waterBlastEffect[20].effectLevel=713.708984
    dbObj.waterBlastEffect[20].damageFactor=0.167000
    dbObj.waterBlastEffect[21].effectLevel=819.270020
    dbObj.waterBlastEffect[21].damageFactor=0.200000
    dbObj.waterBlastEffect[22].effectLevel=948.901978
    dbObj.waterBlastEffect[22].damageFactor=0.250000
    dbObj.waterBlastEffect[23].effectLevel=1116.706055
    dbObj.waterBlastEffect[23].damageFactor=0.333000
    dbObj.waterBlastEffect[24].effectLevel=1357.447998
    dbObj.waterBlastEffect[24].damageFactor=0.500000
    dbObj.waterBlastEffect[25].effectLevel=1800.892944
    dbObj.waterBlastEffect[25].damageFactor=1.000000
    dbObj.waterBlastEffect[26].effectLevel=2322.610107
    dbObj.waterBlastEffect[26].damageFactor=2.000000
    dbObj.waterBlastEffect[27].effectLevel=2967.374023
    dbObj.waterBlastEffect[27].damageFactor=4.000000
    dbObj.fragEffect=[pygcb.DamagePoint()]*25
    dbObj.fragEffect[0].effectLevel=0.000000
    dbObj.fragEffect[0].damageFactor=0.000000
    dbObj.fragEffect[1].effectLevel=1500.000000
    dbObj.fragEffect[1].damageFactor=0.000000
    dbObj.fragEffect[2].effectLevel=3000.000000
    dbObj.fragEffect[2].damageFactor=0.002580
    dbObj.fragEffect[3].effectLevel=6000.000000
    dbObj.fragEffect[3].damageFactor=0.003640
    dbObj.fragEffect[4].effectLevel=10000.000000
    dbObj.fragEffect[4].damageFactor=0.004700
    dbObj.fragEffect[5].effectLevel=30000.000000
    dbObj.fragEffect[5].damageFactor=0.008150
    dbObj.fragEffect[6].effectLevel=60000.000000
    dbObj.fragEffect[6].damageFactor=0.011520
    dbObj.fragEffect[7].effectLevel=100000.000000
    dbObj.fragEffect[7].damageFactor=0.014880
    dbObj.fragEffect[8].effectLevel=300000.000000
    dbObj.fragEffect[8].damageFactor=0.025770
    dbObj.fragEffect[9].effectLevel=600000.000000
    dbObj.fragEffect[9].damageFactor=0.036440
    dbObj.fragEffect[10].effectLevel=1000000.000000
    dbObj.fragEffect[10].damageFactor=0.047050
    dbObj.fragEffect[11].effectLevel=3000000.000000
    dbObj.fragEffect[11].damageFactor=0.081490
    dbObj.fragEffect[12].effectLevel=6000000.000000
    dbObj.fragEffect[12].damageFactor=0.115240
    dbObj.fragEffect[13].effectLevel=10000000.000000
    dbObj.fragEffect[13].damageFactor=0.148780
    dbObj.fragEffect[14].effectLevel=30000000.000000
    dbObj.fragEffect[14].damageFactor=0.257690
    dbObj.fragEffect[15].effectLevel=60000000.000000
    dbObj.fragEffect[15].damageFactor=0.364430
    dbObj.fragEffect[16].effectLevel=100000000.000000
    dbObj.fragEffect[16].damageFactor=0.470480
    dbObj.fragEffect[17].effectLevel=300000000.000000
    dbObj.fragEffect[17].damageFactor=0.814900
    dbObj.fragEffect[18].effectLevel=600000000.000000
    dbObj.fragEffect[18].damageFactor=1.152440
    dbObj.fragEffect[19].effectLevel=1000000000.000000
    dbObj.fragEffect[19].damageFactor=1.487790
    dbObj.fragEffect[20].effectLevel=3000000000.000000
    dbObj.fragEffect[20].damageFactor=2.576930
    dbObj.fragEffect[21].effectLevel=6000000000.000000
    dbObj.fragEffect[21].damageFactor=3.644330
    dbObj.fragEffect[22].effectLevel=10000000000.000000
    dbObj.fragEffect[22].damageFactor=4.704810
    dbObj.fragEffect[23].effectLevel=30000001024.000000
    dbObj.fragEffect[23].damageFactor=8.148970
    dbObj.fragEffect[24].effectLevel=60000002048.000000
    dbObj.fragEffect[24].damageFactor=11.524380
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
    dbObj.internalEffect=[pygcb.DamagePoint()]*9
    dbObj.internalEffect[0].effectLevel=0.000000
    dbObj.internalEffect[0].damageFactor=0.000000
    dbObj.internalEffect[1].effectLevel=1.000000
    dbObj.internalEffect[1].damageFactor=0.115580
    dbObj.internalEffect[2].effectLevel=2.000000
    dbObj.internalEffect[2].damageFactor=0.231010
    dbObj.internalEffect[3].effectLevel=4.000000
    dbObj.internalEffect[3].damageFactor=0.462270
    dbObj.internalEffect[4].effectLevel=8.000000
    dbObj.internalEffect[4].damageFactor=0.924180
    dbObj.internalEffect[5].effectLevel=16.000000
    dbObj.internalEffect[5].damageFactor=1.848800
    dbObj.internalEffect[6].effectLevel=32.000000
    dbObj.internalEffect[6].damageFactor=3.697020
    dbObj.internalEffect[7].effectLevel=64.000000
    dbObj.internalEffect[7].damageFactor=7.395180
    dbObj.internalEffect[8].effectLevel=128.000000
    dbObj.internalEffect[8].damageFactor=14.790390
    return dbObj
