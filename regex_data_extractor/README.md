In this assignment I was suppossed to write regex expression that will be checking pages looking for the required informations.
Require informations are emails, phone number, urls, hashtag, card number,time, html tags and currencies. Each of these required informations are suppossed to be in a valid format, if its not in valid format then it will not be recorded at the output file.
My work is arranged in modules. 
My modules are 
-extractor.py
-patterns.py
-tests/test_patterns.py
 Apart from modules I also have docs as my directory containing sample_output.txt which record the valid output out of text pages.
Extractor.py works like my main file as it is the entry point of everything.
Run extractor.py to test how it works
My regular expressions have been implemented with python.
For running it;
./extractor.py all "write your text here"4
