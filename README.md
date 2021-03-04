# MIMO-for-pattern-recodnition

## Abstract
***
MIMO or Multiple Input Multiple Output, is a technique to increase the link reliability, the spectral efficiency, or both by using multiple antennas at both the transmitter and the receiver in wireless communication. In this assignment, the concept of an uncorrelated MIMO channel of the wireless link is applied to five RGB images of different objects. Firstly the images are converted into gray images and then resized into $16x16$ matrices. These $16 ✕ 16$ image matrices are used as the MIMO channel matrix and the received signal vector under the one-to-one relation for each image that has sixteen eigenvalues is considered as the feature of the corresponding image.

## Basic theory of Eigen decomposition under MIMO
***
A MIMO system consists of several transmit and receive antennas. It is considered a system with $n_T$ transmit and $n_R$ receive antennas. The channel of this system is defined by an $n_R✕ n_T$ matrix, that is denoted by $H$, as a complex matrix. The transmitted signal is represented by an $n_T ✕ 1$ column matrix, denoted by symbol $x$, whereas the received signal is represented by an $n_R ✕ 1$ column matrix, denoted by symbol $r$. 
