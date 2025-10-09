# -*- coding: utf-8 -*-
"""
Created on Thu Oct  9 13:17:40 2025

@author: Augusto
"""

import numpy as np
from scipy import signal as sig
import matplotlib.pyplot as plt
import scipy.io as sio
from scipy.signal import windows
from numpy.fft import fft

#cte universales 
fs_ecg = 1000 # Hz
fs_ppg = 400 # Hz

#funciones de ingreso
#Ecg sin ruido 
ecg_one_lead = np.load('ecg_sin_ruido.npy')
plt.figure()
plt.plot(ecg_one_lead)
plt.title('ecg')
Necg=ecg_one_lead.shape[0]
#La cucaracha
fs_audio, wav_data = sio.wavfile.read('la cucaracha.wav')
plt.figure()
plt.plot(wav_data)
plt.title('La cucaracha')
Ncuca=wav_data.shape[0]
#PPG
ppg = np.load('ppg_sin_ruido.npy')
plt.figure()
plt.plot(ppg)
plt.title('ppg')
Nppg=ppg.shape[0]
#otra aca

# #welch Ecg sin ruido
# cpECG=15 #cantidad de promedio
# npersegECG=ecg_one_lead.shape[0] // cpECG
# print("cantidad:",npersegECG)
# nfft=100*npersegECG
# win='hann'
# tWECGSR_ECG,WECGSR_ECG=sig.welch(ecg_one_lead,fs=fs_ecg,window=win,nperseg=npersegECG,nfft=nfft)
# plt.figure()
# plt.plot(tWECGSR_ECG,(WECGSR_ECG))
# plt.xlim(0,50)
# plt.title("Densidad espectral de potencia (Welch)")
# plt.xlabel("Frecuencia [Hz]")
# plt.ylabel("PSD [V²/Hz]")
# plt.show()
# plt.figure()
# plt.plot(tWECGSR_ECG,10*np.log10(WECGSR_ECG))
# plt.title("Densidad espectral de potencia (Welch)")
# plt.xlabel("Frecuencia [Hz]")
# plt.ylabel("PSD [dB/Hz]")
# plt.show()
# #calculo de varianza acumulada 
# reescalado_ECG=WECGSR_ECG*1e-6
# dfECG_ECG=np.diff(tWECGSR_ECG)
# dfECG_ECG=np.r_[dfECG_ECG, dfECG_ECG[-1]]
# mascara=tWECGSR_ECG <= 50
# var_acumECG=np.cumsum(reescalado_ECG[mascara]*dfECG_ECG[mascara])
# VarnormECG=var_acumECG/var_acumECG[-1] #varianza normalizada
# p=0.99
# idx = np.searchsorted(VarnormECG, p)  # índice donde la curva ≥ p
# BWECG = tWECGSR_ECG[idx]                  # frecuencia de corte (float)
# plt.figure()
# plt.plot(tWECGSR_ECG,(WECGSR_ECG))
# plt.xlim(0,50)
# plt.title("Densidad espectral de potencia (Welch)")
# plt.xlabel("Frecuencia [Hz]")
# plt.ylabel("PSD [V²/Hz]")
# plt.axvline(BWECG)
# plt.show()
# print("Ancho d banda:", BWECG)
# print("Varianza total:", var_acumECG[-1])

# #blackman-tuky ECG 
# #Hago autocorrelacion
# Ecgxx = ecg_one_lead - np.mean(ecg_one_lead)
# Recg=sig.correlate(Ecgxx,Ecgxx, mode='full')/Necg
# lagsecg = np.arange(-Necg+1, Necg)
# centerecg = len(Recg)//2
# M= int(1.0 * fs_ecg)
# Recg_seg = Recg[centerecg-M : centerecg+M+1]
# #ventaneo por la ventana triangular
# Recgventaneada=Recg_seg*sig.windows.bartlett(2*M+1)   
# #le calculo la FFT
# FFTECG=fft(Recgventaneada,axis=0, n=4*Necg)

# plt.figure()
# plt.plot(np.abs(FFTECG))
# plt.xlim([0,10000])
# plt.title('ecg')

# ## La cucaracha welch
# cpcucaracha=20 #cantidad de promedio
# npersegcucaracha=wav_data.shape[0] // cpcucaracha
# print(npersegcucaracha)
# nfftcucaracha=3*npersegcucaracha
# win='hann'
# tWCuca,WCuca=sig.welch(wav_data,fs=fs_audio,window=win,nperseg=npersegcucaracha,nfft=nfftcucaracha)
# plt.figure()
# plt.plot(tWCuca,(WCuca))
# plt.xlim(750,2500)
# plt.title("Densidad espectral de potencia (Welch)")
# plt.xlabel("Frecuencia [Hz]")
# plt.ylabel("PSD [V²/Hz]")
# plt.show()
# plt.figure()
# plt.plot(tWCuca,10*np.log10(WCuca))
# plt.title("Densidad espectral de potencia (Welch)")
# plt.xlabel("Frecuencia [Hz]")
# plt.ylabel("PSD [dB/Hz]")
# plt.show() 
# #calculo de varianza acumulada 
# reescalado=WCuca*1e+5

# dfECG=np.diff(tWCuca)
# dfECG=np.r_[dfECG, dfECG[-1]]
# mascaracuca=tWCuca<=2200
# f_cut = tWCuca[mascaracuca]
# var_acumECG=np.cumsum(reescalado[mascaracuca]*dfECG[mascaracuca])
# VarnormECG=var_acumECG/var_acumECG[-1] #varianza normalizada
# p=0.99
# idx = np.searchsorted(VarnormECG, p)  # índice donde la curva ≥ p
# Bcuca =  f_cut[idx]                # frecuencia de corte (float)
# print("Ancho d banda:", Bcuca)
# print("Varianza total:", var_acumECG[-1])
# plt.figure()
# plt.plot(tWCuca,(WCuca))
# plt.xlim(750,2500)
# plt.title("Densidad espectral de potencia (Welch)+corte")
# plt.xlabel("Frecuencia [Hz]")
# plt.ylabel("PSD [V²/Hz]")
# plt.axvline(Bcuca)
# plt.show()

# #Blackman-turkey 
# #Hago autocorrelacion
# y = wav_data
# if y.ndim > 1:
#     y = y[:, 0]
# y = y.astype(float) - np.mean(y)

# Ncu = len(y)
# Rcu = sig.correlate(y, y, mode='full') / Ncu          # biased
# center_cu = len(Rcu) // 2

# # elegir M en tiempo -> 0.5 s (ejemplo razonable para audio)
# M_des_cu = int(0.5 * fs_audio)
# # limitar M por los datos
# M_cu = min(M_des_cu, Ncu-1, center_cu, len(Rcu) - center_cu - 1)

# Rcu_seg = Rcu[center_cu - M_cu : center_cu + M_cu + 1]
# w_cu = sig.windows.bartlett(len(Rcu_seg))
# Rcu_win = Rcu_seg * w_cu

# nfft_cu = 4 * Ncu
# PSD_BT_cu = np.abs(np.fft.rfft(Rcu_win, n=nfft_cu))

# plt.figure()
# plt.plot(np.abs(PSD_BT_cu))
# plt.xlim(10750,25000)
# plt.title('ecg')

#welche ppg

cpppg=30 #cantidad de promedio
npersegPPG=ppg.shape[0] //cpppg
print("cantidad:",npersegPPG)
nfft=100*npersegPPG
win='hann'
tWPPG,WPPG=sig.welch(ppg,fs=fs_ppg,window=win,nperseg=npersegPPG,nfft=nfft)
plt.figure()
plt.plot(tWPPG,(WPPG))
plt.xlim(0,25)
plt.title("Densidad espectral de potencia (Welch) de la PPG")
plt.xlabel("Frecuencia [Hz]")
plt.ylabel("PSD [V²/Hz]")
plt.show()
plt.figure()
plt.plot(tWPPG,10*np.log10(WPPG))
plt.title("Densidad espectral de potencia (Welch)")
plt.xlabel("Frecuencia [Hz]")
plt.ylabel("PSD [dB/Hz]")
plt.show()
#calculo de varianza acumulada 
reescalado_PPG=WPPG*1e-6
dfECG_PPG=np.diff(tWPPG)
dfECG_PPG=np.r_[dfECG_PPG, dfECG_PPG[-1]]
mascara=tWPPG <= 50
var_acumPPG=np.cumsum(reescalado_PPG[mascara]*dfECG_PPG[mascara])
VarnormECG=var_acumPPG/var_acumPPG[-1] #varianza normalizada
p=0.99
idx = np.searchsorted(VarnormECG, p)  # índice donde la curva ≥ p
BWPPG = tWPPG[idx]                  # frecuencia de corte (float)
plt.figure()
plt.plot(tWPPG,(WPPG))
plt.xlim(0,25)
plt.title("Densidad espectral de potencia (Welch)")
plt.xlabel("Frecuencia [Hz]")
plt.ylabel("PSD [V²/Hz]")
plt.axvline(BWPPG)
plt.show()
print("Ancho d banda:", BWPPG)
print("Varianza total:", var_acumPPG[-1])

# #blackman-tuky PPG 
#Hago autocorrelacion
PPGxx = ppg - np.mean(ppg)
Rppg=sig.correlate(PPGxx,PPGxx, mode='full')/Nppg
lagsecg = np.arange(-Nppg+1, Nppg)
centerppg = len(Rppg)//2
M= int(1.0 * fs_ppg)
Rppg_seg = Rppg[centerppg-M : centerppg+M+1]
#ventaneo por la ventana triangular
Recgventaneada=Rppg_seg*sig.windows.bartlett(2*M+1)   
#le calculo la FFT
FFTPPG=fft(Recgventaneada,axis=0, n=4*Necg)
plt.figure()
plt.plot(np.abs(FFTPPG))
plt.xlim([0,10000])
plt.title('ppg')