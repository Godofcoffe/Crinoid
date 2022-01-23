build:
	cython -3 --embed --cplus -o script.cpp src/crid.py
	g++ -Os -I /usr/include/python3.10 script.cpp -l python3.10 -o crid

clean:
	rm script.cpp

install:
	sudo cp ./crid /usr/bin
