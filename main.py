import func/fuzz.py as func

x = func.np.arange(-10, 11, 0.25)
func.triangular(x,  -5, 0, 6)
func.trapecia(x,-4, 1, 6, 9)
func.qauss(x,  0, 5)
func.gauss2(x,  0, 5, 2, 8)
func.bell(x, 7, 3, 0)
func.sigm(x, -5, 3)
func.dsigm(x, -5, 3, 5, 2)
func.psigm(x, -5, 3, 5, 2)
func.zf(x, 0, 3)
func.pif(x, 1, 3, 5, 8)
func.sf(x, 0, 3)