text = """You think you know all about it, then it seems you are wrong
She hit it out of the park before it had even begun
I needed sunshine in the darkness burning out
Well now I know that I'm the fuel and she's the spark
We are bound to each other's hearts
Caught, torn and pulled apart
This love is like wildfire
And to my word now I'll be true
I can't stop this breaking loose
This love is like wildfire
Like wildfire
As feelings arrange deep down inside
Try describing a love you can't design
More and more, every inch of me is holding on
This is it, all the flames are burning strong
We are bound to each other's hearts
Caught, torn and pulled apart
This love is like wildfire
And to my word now I'll be true
I can't stop this breaking loose
This love, is like wildfire
Like… """

def calcul(letter):
    number = text.count(letter)
    return number

total = calcul('k') + calcul('a')
print(total)