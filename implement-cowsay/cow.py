import cowsay
import sys

words = sys.argv[1:]          
message = " ".join(words)     

cowsay.cow(message)