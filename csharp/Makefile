
debug-build:
	docker run --rm -it --name tfcsgen --volumes-from tfdata-latest --workdir /src/tf/generators/csharp tfcsgen /bin/bash

build: update-data
	docker run --name tfdata-latest -v /src/tf tfdata
	docker run --rm --name tfcsgen --volumes-from tfdata-latest --workdir /src/tf/generators/csharp tfcsgen python2 generate_csharp_bindings.py
	docker run --rm --name tfcsgen --volumes-from tfdata-latest --workdir /src/tf/generators/csharp tfcsgen python2 generate_csharp_zip.py

update-data: clean
	docker build -t tfdata --no-cache --force-rm=true ../

clean:
	docker rm -v tfdata-latest
	docker rmi tfdata
