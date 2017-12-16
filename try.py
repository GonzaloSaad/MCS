
from solver_core.MCSolverPres import MCSolverPres


f = 'A*ln(x+1)+B*x'
x = [0,1,1,2,3,4.5,5]
y = [0,2,3,5,8,12,12.5]

m = MCSolverPres(x,y,f)

print(m.solve())