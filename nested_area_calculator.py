'''
Program Name: Nested Area Calculator

Description:
Calculates the area of different geometric shapes (Circle, Rectangle, Triangle)
using nested functions inside a main function.
Demonstrates the concept of function inside another function and menu-driven execution.

Author: Hamida Badamdi

'''
#Outer function
def area_calc():
    
    
    # Inner function → Circle area
    def circle_area(r):
        return 3.14 * r * r
    
    # Inner function → Rectangle area
    def rectangle_area(l,w):
        return l * w

    # Inner function → Rectangle area
    def triangle_area(b,h):
        return b * h

    while True:
        print("\n=========================================================")
        choice=int(input("\n******Choose shape******\n1.Circle\n2.Rectangle\n3.Triangle\n4.Exit\nEnter your choice: "))

        if choice == 1:
            r=float(input("Enter radius: "))
            print("Area of circle = ",round(circle_area(r),3))
            
        elif choice == 2:
            l=float(input("Enter Length: "))
            w=float(input("Enter Width: "))
            print("Area of rectangle = ",round(rectangle_area(l,w),3))
        
        elif choice == 3:
            b=float(input("Enter base: "))
            h=float(input("Enter height: "))
            print("Area of triangle = ",round(triangle_area(b,h),3))
            
        elif choice == 4:
            print("\nExiting....")
            break
        
        else:
            print("\nInvalid choice!")
        
#calling outer function    
area_calc()
