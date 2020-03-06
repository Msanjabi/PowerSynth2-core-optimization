'''
Created on Feb 17, 2014

@author: shook

Rectangular Flux Channel Model
Closed-form equation based thermal model, steady state temperature estimation
'''
import time
from math import pi, sin, cos, sinh, cosh, sqrt, exp
    
class Baseplate:
    def __init__(self, width, length, thickness, conv_coeff, thermal_cond):
        """
        Represents a baseplate for rect. heat flux thermal model.
        
        Keyword arguments:
        width         float: Dimension of baseplate along x-axis (m)
        length        float: Dimension of baseplate along y-axis (m)
        thickness     float: Dimension of baseplate along z-axis (m)
        conv_coeff    float: Convection coefficient at bottom of plate (W*(m^-2)*(K^-1))
        thermal_cond     float: Thermal conductivity of material (W*(m^-1)*(K^-1))
        """
        self.width = width
        self.length = length
        self.thickness = thickness
        self.conv_coeff = conv_coeff
        self.thermal_cond = thermal_cond

class ExtaLayer:
    def __init__(self, thickness, thermal_cond):
        """
        Represents extra layer on top of baseplate for rect. heat flux thermal model.
        
        Keyword arguments:
        thickness     float: Dimension along z-axis (m)
        thermal_cond  float: Thermal conductivity of material (W*(m^-1)*(K^-1))
        """
        self.thickness = thickness
        self.thermal_cond = thermal_cond

class Device:
    def __init__(self, width, length, center, Q):
        """
        Represents a device for rect. heat flux thermal model.
        
        Keyword arguments:
        width     float: Dimension of device along x-axis (m)
        length    float: Dimension of device along y-axis (m)
        center    tuple (Xc, Yc): Center position of device (m)
        Q         float: Heat flow generated by device (W)
        """
        self.width = width
        self.length = length
        self.center = center
        self.Q = Q
        
def single_layer_top_surface_pt(baseplate, devices, x, y):
    # Baseplate symbols
    a = baseplate.width
    b = baseplate.length
    t1 = baseplate.thickness
    k1 = baseplate.thermal_cond
    h = baseplate.conv_coeff
    
    def lam(m):
        return m*pi/a
    
    def delta(n):
        return n*pi/b
    
    def phi(z):
        top = z*sinh(z*t1) + (h/k1)*cosh(z*t1)
        bot = z*cosh(z*t1) + (h/k1)*sinh(z*t1)
        return top/bot
    
    def A1(m, Xc, c, Q):
        lam_m = lam(m)
        sym = sin(0.5*(2.0*Xc + c)*lam_m) - sin(0.5*(2.0*Xc - c)*lam_m)
        return 2.0*Q*sym/(a*b*c*k1*lam_m**2.0*phi(lam_m))
    
    def A2(n, Yc, d, Q):
        del_n = delta(n)
        sym = sin(0.5*(2.0*Yc + d)*del_n) - sin(0.5*(2.0*Yc - d)*del_n)
        return 2.0*Q*sym/(a*b*d*k1*del_n**2.0*phi(del_n))
    
    def A3(m, n, Xc, Yc, c, d, Q):
        lam_m = lam(m)
        del_n = delta(n)
        beta_mn = sqrt(lam_m**2.0 + del_n**2.0)
        top = 16.0*Q*cos(lam_m*Xc)*sin(0.5*lam_m*c)*cos(del_n*Yc)*sin(0.5*del_n*d)
        return top/(a*b*c*d*k1*beta_mn*lam_m*del_n*phi(beta_mn))
    
    def theta(device, res=5):
        Xc, Yc = device.center
        c = device.width
        d = device.length
        Q = device.Q
        
        A0 = (Q/(a*b))*(t1/k1 + 1.0/h)
    
        Am_comp = 0.0
        for m in range(1, res):
            Am_comp += A1(m, Xc, c, Q)*cos(lam(m)*x)
            
        An_comp = 0.0
        for n in range(1, res):
            An_comp += A2(n, Yc, d, Q)*cos(delta(n)*y)
            
        Amn_comp = 0.0
        for m in range(1, res):
            for n in range(1, res):
                Amn_comp += A3(m, n, Xc, Yc, c, d, Q)*cos(lam(m)*x)*cos(delta(n)*y)
                
        return A0 + Am_comp + An_comp + Amn_comp
    
    theta_sum = 0.0
    for device in devices:
        theta_sum += theta(device, 25)
        
    return theta_sum

def single_layer_top_surface_avg(baseplate, devices, dev_index):
    # Baseplate symbols
    a = baseplate.width
    b = baseplate.length
    t1 = baseplate.thickness
    k1 = baseplate.thermal_cond
    h = baseplate.conv_coeff
    
    def lam(m):
        return m*pi/a
    
    def delta(n):
        return n*pi/b
    
    def phi(z):
        top = z*sinh(z*t1) + (h/k1)*cosh(z*t1)
        bot = z*cosh(z*t1) + (h/k1)*sinh(z*t1)
        return top/bot
    
    def A1(m, Xc, c, Q):
        lam_m = lam(m)
        sym = sin(0.5*(2.0*Xc + c)*lam_m) - sin(0.5*(2.0*Xc - c)*lam_m)
        return 2.0*Q*sym/(a*b*c*k1*lam_m**2.0*phi(lam_m))
    
    def A2(n, Yc, d, Q):
        del_n = delta(n)
        sym = sin(0.5*(2.0*Yc + d)*del_n) - sin(0.5*(2.0*Yc - d)*del_n)
        return 2.0*Q*sym/(a*b*d*k1*del_n**2.0*phi(del_n))
    
    def A3(m, n, Xc, Yc, c, d, Q):
        lam_m = lam(m)
        del_n = delta(n)
        beta_mn = sqrt(lam_m**2.0 + del_n**2.0)
        top = 16.0*Q*cos(lam_m*Xc)*sin(0.5*lam_m*c)*cos(del_n*Yc)*sin(0.5*del_n*d)
        return top/(a*b*c*d*k1*beta_mn*lam_m*del_n*phi(beta_mn))
    
    def theta_avg(device, target_device, res=5):
        Xc, Yc = device.center
        c = device.width
        d = device.length
        Q = device.Q
        
        Xcj, Ycj = target_device.center
        cj = target_device.width
        dj = target_device.length
        
        A0 = (Q/(a*b))*(t1/k1 + 1.0/h)
    
        Am_comp = 0.0
        for m in range(1, res):
            Am_comp += A1(m, Xc, c, Q)*cos(lam(m)*Xcj)*sin(0.5*lam(m)*cj)/(lam(m)*cj)
        Am_comp *= 2.0
            
        An_comp = 0.0
        for n in range(1, res):
            An_comp += A2(n, Yc, d, Q)*cos(delta(n)*Ycj)*sin(0.5*delta(n)*dj)/(delta(n)*dj)
        An_comp *= 2.0
            
        Amn_comp = 0.0
        for m in range(1, res):
            for n in range(1, res):
                top = cos(delta(n)*Ycj)*sin(0.5*delta(n)*dj)*cos(lam(m)*Xcj)*sin(0.5*lam(m)*cj)
                bot = lam(m)*cj*delta(n)*dj
                Amn_comp += A3(m, n, Xc, Yc, c, d, Q)*top/bot
        Amn_comp *= 4.0
                
        return A0 + Am_comp + An_comp + Amn_comp
    
    theta_avg_sum = 0.0
    for device in devices:
        theta_avg_sum += theta_avg(device, devices[dev_index], 25)
        
    return theta_avg_sum

def compound_top_surface_avg(baseplate, layer, devices, dev_index, resolution=20):
    # Baseplate symbols
    a = baseplate.width
    b = baseplate.length
    t2 = baseplate.thickness
    k2 = baseplate.thermal_cond
    h = baseplate.conv_coeff
    
    # Extra layer
    t1 = layer.thickness
    k1 = layer.thermal_cond
    
    def lam(m):
        return m*pi/a
    
    def delta(n):
        return n*pi/b
    
    def phi(z):
        kappa = k2/k1
        eta = (z+h/k2)/(z-h/k2)
        alpha = (1-kappa)/(1+kappa)
        top = (alpha*exp(4.0*z*t1)-exp(2.0*z*t1))+eta*(exp(2.0*z*(2.0*t1+t2))-alpha*exp(2.0*z*(t1+t2)))
        bot = (alpha*exp(4.0*z*t1)+exp(2.0*z*t1))+eta*(exp(2.0*z*(2.0*t1+t2))+alpha*exp(2.0*z*(t1+t2)))
        return top/bot
    
    def A1(m, Xc, c, Q):
        lam_m = lam(m)
        sym = sin(0.5*(2.0*Xc + c)*lam_m) - sin(0.5*(2.0*Xc - c)*lam_m)
        return 2.0*Q*sym/(a*b*c*k1*lam_m**2.0*phi(lam_m))
    
    def A2(n, Yc, d, Q):
        del_n = delta(n)
        sym = sin(0.5*(2.0*Yc + d)*del_n) - sin(0.5*(2.0*Yc - d)*del_n)
        return 2.0*Q*sym/(a*b*d*k1*del_n**2.0*phi(del_n))
    
    def A3(m, n, Xc, Yc, c, d, Q):
        lam_m = lam(m)
        del_n = delta(n)
        beta_mn = sqrt(lam_m**2.0 + del_n**2.0)
        top = 16.0*Q*cos(lam_m*Xc)*sin(0.5*lam_m*c)*cos(del_n*Yc)*sin(0.5*del_n*d)
        return top/(a*b*c*d*k1*beta_mn*lam_m*del_n*phi(beta_mn))
    
    def theta_avg(device, target_device, res=20):
        Xc, Yc = device.center
        c = device.width
        d = device.length
        Q = device.Q
        
        Xcj, Ycj = target_device.center
        cj = target_device.width
        dj = target_device.length
        
        A0 = (Q/(a*b))*(t1/k1 + t2/k2 + 1.0/h)
    
        Am_comp = 0.0
        for m in range(1, res):
            Am_comp += A1(m, Xc, c, Q)*cos(lam(m)*Xcj)*sin(0.5*lam(m)*cj)/(lam(m)*cj)
        Am_comp *= 2.0
            
        An_comp = 0.0
        for n in range(1, res):
            An_comp += A2(n, Yc, d, Q)*cos(delta(n)*Ycj)*sin(0.5*delta(n)*dj)/(delta(n)*dj)
        An_comp *= 2.0
            
        Amn_comp = 0.0
        for m in range(1, res):
            for n in range(1, res):
                top = cos(delta(n)*Ycj)*sin(0.5*delta(n)*dj)*cos(lam(m)*Xcj)*sin(0.5*lam(m)*cj)
                bot = lam(m)*cj*delta(n)*dj
                Amn_comp += A3(m, n, Xc, Yc, c, d, Q)*top/bot
        Amn_comp *= 4.0
                
        return A0 + Am_comp + An_comp + Amn_comp
    
    theta_avg_sum = 0.0
    for device in devices:
        theta_avg_sum += theta_avg(device, devices[dev_index], resolution)
        
    return theta_avg_sum

def layer_average(layers):
    total_thick = 0.0
    for layer in layers:
        total_thick += layer[0]
    
    avg_thermal_cond = 0.0
    for layer in layers:
        avg_thermal_cond += (layer[0]/total_thick)*layer[1]
        
    return total_thick, avg_thermal_cond

if __name__ == '__main__':
    bp = Baseplate(width = 50.0e-3,
                   length = 50.0e-3,
                   thickness = 5.0e-3,
                   conv_coeff = 100.0,
                   thermal_cond = 190.0)
    
    met = (0.41, 200.0)
    iso = (0.64, 160.0)
    thickness, thermal_cond = layer_average([met, iso, met])
    print('thickness', thickness)
    print('thermal_cond', thermal_cond)
    layer = ExtaLayer(thickness*1e-3, thermal_cond)
    
    dev1 = Device(width = 10.0e-3,
                 length = 10.0e-3,
                 center = (15.0e-3, 10.0e-3),
                 Q = 10.0)
    
    dev2 = Device(width = 5.0e-3,
                 length = 5.0e-3,
                 center = (30.0e-3, 30.0e-3),
                 Q = 10.0)
    starttime=time.time()
    print(single_layer_top_surface_pt(bp, [dev1, dev2], 15.0e-3, 10.0e-3))
    print(single_layer_top_surface_avg(bp, [dev1, dev2], 1))
    print(compound_top_surface_avg(bp, layer, [dev1, dev2], 0))
    tot_time=time.time()-starttime
    print(tot_time)
    