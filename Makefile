GOOGLEPATH=/mnt/e/cloud-google/opendata

all: build/strassennamen.pdf \
	copy

build/FB62-Straßenliste.csv: FORCE | build
	rm -f $@
	wget https://opendata.dortmund.de/OpenDataConverter/download/Geographie,%20Geologie%20und%20Geobasisidaten/FB62-Stra%C3%9Fenliste.csv -P build

build/strassennamen.pdf: python/strassennamen.py build/FB62-Straßenliste.csv | build
	TEXINPUTS="$$(pwd):" python $^


copy:
	cp build/*.pdf $(GOOGLEPATH)
	cp build/*.png $(GOOGLEPATH)

build:
	mkdir -p build

clean:
	rm -rf build

.PHONY: all clean FORCE copy
