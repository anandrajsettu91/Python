class miscellaneousFunctions():
    def Subfeilds():
        print("Sub-fields in AI are:")
        list1=["Machine Learning","Neural Networks","Vision","Robotics","Speech Processing","Natural Language Processing"]
        for temp in list1:
            print(temp)
            value=temp
        return value

    def oddEven():
        num=int(input("Enter a number:"))
        if(num%2==0):
            result=num,"is even number"
        else:
            result=num,"is odd number"
        return result

    def Elegible():
        gender=input("Your Gender:")
        age=int(input("Your Age:"))
        if((gender=="Male") and (age>=21)):
            message="Elegible for Marriage"
        elif((gender=="Female") and (age>=18)):
            message="Elegible for Marriage"
        else:
            message="Not Elegible for Marriage"
        return message

    def percentageScored():
        sub1=int(input("Subject1"))
        sub2=int(input("Subject2"))
        sub3=int(input("Subject3"))
        sub4=int(input("Subject4"))
        sub5=int(input("Subject5"))
        Total=sub1+sub2+sub3+sub4+sub5
        print("Total:",Total)
        percent=float(Total*100/500)
        print("Percentage:",percent)
        per=("Percentage:",percent)
        return per

    def attributesOfTriangle():
        height=int(input("Height:"))
        breath=int(input("Breath:"))
        print("Area formula: (Height*Breath)/2")
        area=height*breath/2
        print("Area of Triangle:",area)
        h1=int(input("Height1:"))
        h2=int(input("Height2:"))
        b=int(input("Breath:"))
        print("Perimeter formula: Height1+Height2+Breath")
        perimeter=h1+h2+b
        print("Perimeter of Triangle:",perimeter)
        return area
        return perimeter