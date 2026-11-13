

In order to address the concerns around scams and digital arrest cases and many others ,do the panellists view a risk based approach as a proportionate solution. And if so be the case there would still be cases where access to app is denied, would that cost to consumer be justified in the name of safety and security concerns, and even regulatory cost to apps, telcos, etc. 

- 
    
    Anonymous Attendee02:06 PM
    
    ···
    
    I believe SIM binding will happen only for login not regular usage. So it's a one time thing. So it should not matter if user is out of network or only on wifi after successful login. So the point of network is not correct. Also there are multiple forms of SIM binding and I don't think those have been mandated which form of binding apps need to do choose. So there is leeway there to keep it user friendly. UPI apps do binding already (there is no difference between banks and upi apps here) and success rates of some form of binding are as high as 97-98% at attempt basis. Lastly, there are a lot of WhatsApp takeovers that happen where user ends up sharing their WhatsApp login otp or install a malware on their phone and give all OTP access to malware like fake rto challan etc After takeovers, fraudsters message to all the contacts of victim to send them money and hence a lot of users end up losing money. So there is valid case for adding binding or adding slightly stronger controls.
    
    This question has been answered live
    
    Type Answer
    

- 
    
    Anonymous Attendee02:33 PM
    
    ···
    
    iOS does not give capability to check SIM id. Hence once binding is done if the SIM is changed, apps can't track it. Hence Parag was able to change his SIM. However on Android, apps can read SIM id of a SIM. So once binding is done, and apps can just keep checking if the same SIM id is present on device or not. UPI apps already do it at the time of each transaction where they validate if the original SIM on which binding was done is still present or not (OS polling - as Parag mentioned it). btw Apple now has ctCellularPlan API available on iOS 27 which checks if the mobile data of a number is present on device or not. It is publicly available now and apps are already using it.
    
    This question has been answered live
