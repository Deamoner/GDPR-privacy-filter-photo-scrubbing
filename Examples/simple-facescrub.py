#from "../src/privy" import Privy
import sys
sys.path.append('../src/')
import privy

privateer = privy.Privy()
faces2, img = privateer.processFile("../TestPics/1Person-Close.jpg")
print(faces2)
print(img)
