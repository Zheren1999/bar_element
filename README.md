# bar_element

This code numerically solves the problem of non-infinite column resting on non-linear foundation with initial imperfection.

Differential equation for solving solution for non-infinite column resting on non-linear foundation with initial imperfection is:

<img src="https://render.githubusercontent.com/render/math?math=\frac{d^4u}{d\eta^4} %2B \alpha \gamma\frac{d^2u}{d\eta^2}+k_1u-k_3u^3=-\alpha\gamma \frac{d^2u'}{d\eta^2}">

<img src="https://render.githubusercontent.com/render/math?math=u%3D%5Cfrac%7Bw%7D%7B%5Cdelta%7D%2C%20u'%3D%5Cfrac%7Bw'%7D%7B%5Cdelta%7D%2C%5Calpha%3D%5Cfrac%7BP%7D%7BP_c%7D">

<img src="https://render.githubusercontent.com/render/math?math=%5Cgamma%3D%5Cpi%5E2m_c%2B%5Cfrac%7Bk_1%7D%7Bpi%5E2m_c%5E2%7D%2C%20k_1%3D%5Cfrac%7BK_1l%5E4%7D%7BEI%7D%2Ck_3%3D%5Cfrac%7BK_3%5Cdelta%5E2l%5E4%7D%7BEI%7D%2C%5Ceta%3D%5Cfrac%7Bx%7D%7B%5Cdelta%7D">

where <img src="https://render.githubusercontent.com/render/math?math=%24%5Cbar%20w%24"> is the initial deflection, <img src="https://render.githubusercontent.com/render/math?math=%24w%24"> is the additional deflection due to the axial load <img src="https://render.githubusercontent.com/render/math?math=%24P%24">, and <img src="https://render.githubusercontent.com/render/math?math=%24k_1%2C%20k_3%20%3E%200%24"> are the linear and nonlinear ``spring" constants of the foundation. <img src="https://render.githubusercontent.com/render/math?math=%24P%24"> is the axial load.

The solution of differential equation can be represented as series of sine Fourier expansion:

<img src="https://render.githubusercontent.com/render/math?math=u(%5Ceta)%3D%20%5Csum_%7Bm%3D1%7D%5E%7B%5Cinfty%7D%5Cxi_m%20sin(m%5Cpi%5Ceta)">

Infinite imperfection also can be represented the same:

<img src="https://render.githubusercontent.com/render/math?math=u'(%5Ceta)%3D%20%5Csum_%7Bm%3D1%7D%5E%7B%5Cinfty%7D%5Cxi'_m%20sin(m%5Cpi%5Ceta)">

Substitution (4) and (5) in the equation (1):

<img src="https://render.githubusercontent.com/render/math?math=%5Calpha_m%5Cxi_m-%5Calpha(%5Cxi_m%2B%5Cxi'_m)-%5Cfrac%7Bsm_c%5E2I_m%7D%7B8m%5E2%7D%3D0">

where

<img src="https://render.githubusercontent.com/render/math?math=s%3D%5Cfrac%7B2k_3%7D%7Bk_1%2B%5Cpi%5E4m_c%5E4%7D">

<img src="https://render.githubusercontent.com/render/math?math=%5Calpha_m%3D%5Cfrac%7B%5Cpi%5E2m%5E2%2Bk1%2F(%5Cpi%5E2m%5E2)%7D%7B%5Cpi%5E2m_c%5E2%2Bk1%2F(%5Cpi%5E2m_c%5E2%7D">

<img src="https://render.githubusercontent.com/render/math?math=I_m%3D%5Csum_%7Bp%3D1%7D%5E%7B%5Cinfty%7D%5Csum_%7Bq%3D1%7D%5E%7B%5Cinfty%7D%5Csum_%7Br%3D1%7D%5E%7B%5Cinfty%7D%5Cxi_p%5Cxi_q%5Cxi_r%5B%5Cdelta_%7Bp%2Bq%2Cr%2Bm%7D-%5Cdelta_%7B%7Cp-q%7C%2Cr%2Bm%7D-%5Cdelta_%7Bp%2Bq%2C%7Cr-m%7C%7D%2B%5Cdelta_%7B%7Cp-q%7C%2C%7Cr-m%7C%7D%2B%5Cdelta_%7Bp%2Cq%7D%5Cdelta_%7Br%2Cm%7D%5D">
