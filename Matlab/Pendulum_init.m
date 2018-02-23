b1= 0.4;
b2= 0.1;
g = 9.81;
l = 0.5;
r = 1;
m1= 1;
m2= 0.5;
A=[(-b1)/(l*l*m1),(g*m2)/(l*m1),(-b2)/(r*l*m1);0,0,1;(-b1)/(r*l*m1),(g*(m1+m2))/(r*m1),(-b2*(m1+m2))/(r*r*m1*m1)];
B=[1/(l*l*m1);0;1/(l*r*m1)];
[K,S,e]=lqr(A,B,eye(3),eye(1));
K=[0 K];
open('pendulum.mdl')