from graphics import*

#from graphics import circle,rectangle

#from graphics.graphics_3d import sphere,cuboid

r=float(input("Enter radius of circle : "))
print ("circle area = ",circle.circle_area(r))
print ("circle perimeter = ",circle.circle_peri(r))
r=float(input("Enter radius of sphere : "))
print ("sphere perimeter = ",sphere.sphere_area(r))
print ("sphere perimeter = ",sphere.sphere_peri(r))
l=int(input("Enter length of rectagle : "))
b=int(input("Enter breadth of rectangle : "))
print ("rectangle perimeter = ",rectangle.rect_area(l,b))
print ("rectangle perimeter = ",rectangle.rect_peri(l,b))
l=int(input("Enter length of cuboid : "))
b=int(input("Enter breadth of cuboid : "))
h=int(input("Enter height of cuboid"))
print ("cuboid perimeter = ",cuboid.cuboid_area(l,b,h))
print ("cuboid perimeter = ",cuboid.cuboid_peri(l,b,h))
