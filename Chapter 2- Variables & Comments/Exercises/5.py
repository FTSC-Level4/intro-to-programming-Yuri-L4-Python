
#assign budget and cost per piece to variable
Girl_mny_pounds = 50
USB_Stick_price = 6

#make formula to get the quantity and pounds remaining 
USB_amount = Girl_mny_pounds//USB_Stick_price                    
pounds_left = Girl_mny_pounds%USB_Stick_price                   

#print the output answer
print("\n", "The girl can buy", USB_amount, "USB sticks.", "\n "
      "And she will have", pounds_left ," Pounds left.", "\n")





