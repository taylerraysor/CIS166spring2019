from graphics import *

def main():
    win = GraphWin("poundsToMetricFunction converter" , 900,1000)
    Text(Point(100,150), "kilograms converter:") .draw(win)
    Text(Point(250,400), "grams converter:") .draw(win)
    Text(Point(450,500), "ounce converter:") .draw(win)
    inputText = Entry(Point(25,30), 3)
    inputText.setText("0.0")
    inputText.draw(win)
    button1 = Text(Point(100,150), "Convert it")
    button1.draw(win)
    button2 = Text(Point(300,450), "Convert it")
    button2.draw(win)
    button3 = Text(Point(500,550), "Convert it")
    button3.draw(win)
    # wait for a mouse click
    win.getMouse()
    # convert input
    pounds = float(inputText.getText())
    kilograms = pounds / 2.2
    grams = kilograms * 1000
    ounce = grams * 35.274
    # wait for a mouse click
    win.getMouse()
    
main()
    
    
def poundsToMetricFunction(kilograms, grams, ounce):
    pounds = float(input("Enter the amount of pounds:  "))
    kilograms = pounds / 2.2 
    grams = kilograms * 1000
    ounce = grams * 35.274
    print("The amount of pounds you entered is:  ", pounds, 'Converts to' , grams, 'Converts to' , kilograms, 'Converts to' , ounce)

poundsToMetricFunction(250,450)

