cl__1 = 1;
Point(1) = {0, 10, 0, cl__1};
Point(2) = {30, 10, 0, cl__1};
Point(3) = {30, 0, 0, cl__1};
Point(4) = {0, 0, 0, cl__1};
Point(5) = {10, 5, 0, cl__1};
Point(6) = {10, 7.0, 0, cl__1};
Point(7) = {13.0, 5, 0, cl__1};
Point(8) = {10, 3.0, 0, cl__1};
Point(9) = {7.0, 5, 0, cl__1};
Line(1) = {1, 2};
Line(2) = {2, 3};
Line(3) = {3, 4};
Line(4) = {4, 1};
Ellipse(5) = {9, 5, 6};
Ellipse(6) = {6, 5, 7};
Ellipse(7) = {7, 5, 8};
Ellipse(8) = {8, 5, 9};
Line Loop(16) = {5, 6, 7, 8, -3, -2, -1, -4};
Plane Surface(16) = {16};

Physical Line(4) = {5, 6, 7, 8};
Physical Line(3) = {1};
Physical Line(5) = {3};
Physical Line(1) = {4};
Physical Line(2) = {2};
Physical Surface(17) = {16};
