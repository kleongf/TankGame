import math

class Projectile:
    def __init__(self, x, y, angle, speed):
       
        self.x = x  
        self.y = y  
        self.angle = angle  
        self.speed = speed  
        self.velocity_x = speed * math.cos(angle) 
        self.velocity_y = speed * math.sin(angle)  
    
    def update(selfpos, delta_time):
       
        
        selfpos.x += selfpos.velocity_x * delta_time
        selfpos.y += selfpos.velocity_y * delta_time
    
    def check_bounds(self, width, height):
       
        return self.x < 0 or self.x > width or self.y < 0 or self.y > height
    
    
    
    def render(self, screen):
       
       pass
        


