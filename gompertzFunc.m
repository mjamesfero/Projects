function dxdt = gompertzFunc(t,x,r,K)
% function dxdt = gompertzFunc(t,x,r,K)
%
% This is the right hand side of the Gompertz IVP model.
% This is copied from logisticFunc.m because the idea is the same.
%
% inputs:
%   (t,x) = time and space
%   r     = growth rate parameter
%   K     = carrying capacity parameter
%
% output:
%   dxdt = derivative (right hand side of ODE)

dxdt = r*x*log(K/x);

end