%% Parameters
r = .5;
x01 = 10;

%% Experimental Data
time = [0.30143, 1.02690, 2.52690, 3.40190, 4.97548];
amount = [11.62663, 16.71048, 35.37610, 54.79157, 120.34026];
t0 = 0;
tf = 5;

%% Solve ODE
[T1,X1] = ode45(@(t,x) exponentialFunc(t,x,r),[t0,tf],x01);

%% Plots
scatter(time,amount,'r')
hold on
plot(T1,X1,'m','LineWidth',1.5)
hold off

xlabel('t')
ylabel('x(t)')
title('Exponential Equation')

legend('experiment', 'r=0.5')