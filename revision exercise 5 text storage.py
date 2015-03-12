import pickle

class Text:

     with open("text.txt", mode = "w", encoding = "utf-8") as text_file:


        text1 = input("enter text: ")
        text_file.write("{0}\n".format(text1))
        
        text2 = input("enter text: ")
        text_file.write("{0}\n".format(text2))
        
        text3 = input("enter text: ")
        text_file.write("{0}\n".format(text3))
        
        text4 = input("enter text: ")
        text_file.write("{0}\n".format(text4))
        
        text5 = input("enter text: ")
        text_file.write("{0}\n".format(text5))


   
           


