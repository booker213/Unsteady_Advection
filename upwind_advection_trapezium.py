from firedrake import *
m=20
tmesh = Mesh("trapezium_trans.msh")


V = FunctionSpace(tmesh, "DG", 0)
W = VectorFunctionSpace(tmesh, "CG", 1)

timestep = 0.05




# Advection velocity
velocity = Expression(("1.0",  "1.0"))
u0 = project(velocity, W)
#Inflow BC
inflow = Expression("(x[1] < 0.2) && (x[0] < 0.5) ? 1.0 : 0")
#Inflow Variable
D0 = Function(V)
D0.interpolate(inflow)

#Initial Condition
ic = Expression("(x[1] = 0.0 ) && (x[0] < 0.5) ? 1.0 : 0")

#Set up element normal
n = FacetNormal(tmesh)
#
un = 0.5*(dot(u0, n) + abs(dot(u0, n)))

#Previous timestep for BE timestep
D_=Function(V)

D_.interpolate(ic)

D = TrialFunction(V)
phi = TestFunction(V)

# Setting up Bilinear form
a1 = ((D/timestep)*phi - D*dot(u0, grad(phi)))*dx 
a2 = dot(jump(phi), un('+')*D('+') - un('-')*D('-'))*dS #Internal flux
a3 = dot(phi, un*D)*(ds(111)+ds(112))   # outflow at top wall
a = a1 + a2 + a3

L = (D_/timestep)*phi*dx - D0*phi*dot(u0, n)*(ds(114)+ds(113))  # inflow at bottom wall and previous timestep


out = Function(V)




outfile = File("upwind_unsteady.pvd")
# Write IC to file
outfile << D_
t=0.0
end=1
while (t <= end):
       #Solve problem
       solve(a == L, out)
	   #Update previous timestep
       D_.assign(out)
	   #Update time
       t+=timestep
       outfile << out

