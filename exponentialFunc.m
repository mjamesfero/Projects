function dxdt = exponentialFunc(t,x,r)
% function dxdt = exponentialFunc(t,x,r)
% Righthand side of ODE in HW2 Problem 6.
%inputs:
%   (t,x) = time and space
%    r    = growth rate parameter
% output:
%   dxdt = derivative (right hand side of ODE)

dxdt = r*x;
end