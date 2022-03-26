%% Parameters
r = 0.4;
K = 230;

%% Initial Condition and Time Interval
x01 = 100;
x02 = 500;
x03 = -100;
t0 = 0;
tf = 20;

%% Solve ODE
[T1,X1] = ode45(@(t,x) gompertzFunc(t,x,r,K),[t0,tf],x01);
[T2,X2] = ode45(@(t,x) gompertzFunc(t,x,r,K),[t0,tf],x02);
[T3,X3] = ode45(@(t,x) gompertzFunc(t,x,r,K),[t0,tf],x03);

%% Plots
plot(T1,X1,'r','LineWidth',1.5)
hold on
plot(T2,X2,'m','LineWidth',1.5)
%plot(T3,X3,'b','LineWidth',1.5) commented out for being unphysical
hold off

xlabel('t')
ylabel('x(t)')
title('Gompertz Equation')

legend('Initial x=100','Initial x=500','Initial x=-100')