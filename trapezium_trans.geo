Merge "trapezium.3-Linux/bin/trapezium";
e_w =0.1;
Point(1) = {0, 0, 0, e_w};
Point(2) = {0.7, 0, 0, e_w};
Point(3) = {1, 1, 0, e_w};
Point(4) = {0, 1, 0, e_w};
Line(1) = {4, 1};
Line(2) = {2, 3};
Line(3) = {4, 3};
Line(4) = {1, 2};
Line Loop(5) = {3, -2, -4, -1};
Plane Surface(6) = {5};
Physical Surface(7) = {6};

Transfinite Line{1:4} = 51;
Transfinite Surface{6} = {1,2,3,4};
Recombine Surface{6};

Physical Surface(7) = {6};

Physical Line(111) = {3};
Physical Line(113) = {1};
Physical Line(114) = {4};
Physical Line(112) = {2};


