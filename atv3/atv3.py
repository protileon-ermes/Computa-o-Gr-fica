import numpy as np
import cv2
from matplotlib import pyplot as plt

arara = cv2.imread('atv3/arara.png', 0)
b1 = cv2.imread('atv3/barra1.png', 0)
b2 = cv2.imread('atv3/barra2.png', 0)
b3 = cv2.imread('atv3/barra3.png', 0)
b4 = cv2.imread('atv3/barra4.png', 0)
quad = cv2.imread('atv3/quadrado.png', 0)
test = cv2.imread('atv3/teste.png', 0)

araraS = cv2.dft(np.float32(arara),flags = cv2.DFT_COMPLEX_OUTPUT)
b1S = cv2.dft(np.float32(b1),flags = cv2.DFT_COMPLEX_OUTPUT)
b2S = cv2.dft(np.float32(b2),flags = cv2.DFT_COMPLEX_OUTPUT)
b3S = cv2.dft(np.float32(b3),flags = cv2.DFT_COMPLEX_OUTPUT)
b4S = cv2.dft(np.float32(b4),flags = cv2.DFT_COMPLEX_OUTPUT)
quadS = cv2.dft(np.float32(quad),flags = cv2.DFT_COMPLEX_OUTPUT)
testS = cv2.dft(np.float32(test),flags = cv2.DFT_COMPLEX_OUTPUT)

araraDFT = np.fft.fftshift(araraS)
b1DFT = np.fft.fftshift(b1S)
b2DFT = np.fft.fftshift(b2S)
b3DFT = np.fft.fftshift(b3S)
b4DFT = np.fft.fftshift(b4S)
quadDFT = np.fft.fftshift(quadS)
testDFT = np.fft.fftshift(testS)

araraMag = 20 * np.log(cv2.magnitude(araraDFT[:,:,0], araraDFT[:,:,1]) + 1e-10)
b1Mag = 20 * np.log(cv2.magnitude(b1DFT[:,:,0], b1DFT[:,:,1]) + 1e-10)
b2Mag = 20 * np.log(cv2.magnitude(b2DFT[:,:,0], b2DFT[:,:,1]) + 1e-10)
b3Mag = 20 * np.log(cv2.magnitude(b3DFT[:,:,0], b3DFT[:,:,1]) + 1e-10)
b4Mag = 20 * np.log(cv2.magnitude(b4DFT[:,:,0], b4DFT[:,:,1]) + 1e-10)
quadMag = 20 * np.log(cv2.magnitude(quadDFT[:,:,0], quadDFT[:,:,1]) + 1e-10)
testMag = 20 * np.log(cv2.magnitude(testDFT[:,:,0], testDFT[:,:,1]) + 1e-10)

plt.figure(figsize=(9,9)) 
plt.subplot(241)
plt.imshow(araraMag, cmap="gray"); plt.axis('off'); plt.title('arara')
plt.subplot(242)
plt.imshow(b1Mag, cmap="gray"); plt.axis('off'); plt.title('barra 1')
plt.subplot(243)
plt.imshow(b2Mag, cmap="gray"); plt.axis('off'); plt.title('barra 2')
plt.subplot(244)
plt.imshow(b3Mag, cmap="gray"); plt.axis('off'); plt.title('barra 3')
plt.subplot(245)
plt.imshow(b4Mag, cmap="gray"); plt.axis('off'); plt.title('barra 4')
plt.subplot(246)
plt.imshow(quadMag, cmap="gray"); plt.axis('off'); plt.title('quadrado')
plt.subplot(247)
plt.imshow(testMag, cmap="gray"); plt.axis('off'); plt.title('teste')

plt.show()

testN = testS.shape[0]//2
testM = testS.shape[1]//2

testP1 = np.fft.fftshift(testS).copy()
testP1[testN-9:testN+9, testM-9:testM+9] = 0 #passa alta
testP1 = np.fft.ifftshift(testP1)
img_back1 = cv2.idft(testP1, flags=cv2.DFT_SCALE | cv2.DFT_REAL_OUTPUT)#)


testP2 = np.fft.fftshift(testS).copy()
testP2[:testN-9, :] = 0 # passa baixa
testP2[:, :testM-8] = 0 
testP2[testN+7:, :] = 0
testP2[:, testM+6:] = 0
testP2 = np.fft.ifftshift(testP2)
img_back2 = cv2.idft(testP2, flags=cv2.DFT_SCALE | cv2.DFT_REAL_OUTPUT)#)


testP3 = testS.copy()
testP3[testN-5:testN+5, testM-5:testM+5] = 0 #rejeita banda
testP3[:testN-7, :] = 0
testP3[testN+7:,:] = 0
testP3[:, :testM-7] = 0
testP3[:, testM+7:] = 0
testP3 = np.fft.ifftshift(testP3)
img_back3 = cv2.idft(testP3, flags=cv2.DFT_SCALE | cv2.DFT_REAL_OUTPUT)#)


plt.subplot(334)
plt.imshow(img_back1, cmap="gray")
plt.axis('off'); plt.title('passa alta')
plt.subplot(335)
plt.imshow(img_back2, cmap="gray")
plt.axis('off'); plt.title('passa baixa')
plt.subplot(336)
plt.imshow(img_back3, cmap="gray")
plt.axis('off'); plt.title('rejeita banda')

plt.show()