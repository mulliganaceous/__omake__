#!/bin/bash
echo "#!/bin/bash" > omg1.sh
echo "omg1"
find -maxdepth 2 -name "../backups/*.exe" >> omg1.sh
find -maxdepth 2 -name "*.a" >> omg1.sh
find -maxdepth 2 -name "*.h" >> omg1.sh
find -maxdepth 2 -name "*.c" >> omg1.sh

echo "#!/bin/bash" > omg2.sh
echo "omg2"
find -maxdepth 2 -name "*.dll" >> omg2.sh
find -maxdepth 2 -name "*.ini" >> omg2.sh
find -maxdepth 2 -name "*.ico" >> omg2.sh
find -maxdepth 2 -name "*.jar" >> omg2.sh
find -maxdepth 2 -name "*.jsp" >> omg2.sh
find -maxdepth 2 -name "*.html" >> omg2.sh
find -maxdepth 2 -name "*.java" >> omg2.sh
find -maxdepth 2 -name "*.reg" >> omg2.sh
find -maxdepth 2 -name "*.ttf" >> omg4.sh

echo "#!/bin/bash" > omg3.sh
echo "omg3"
find -maxdepth 2 -name "*.txt" >> omg3.sh
find -maxdepth 2 -name "*.bat" >> omg3.sh

echo "#!/bin/bash" > omg4.sh
echo "omg4"
find -maxdepth 2 -name "*.pyc" >> omg4.sh
find -maxdepth 2 -name "*.xml" >> omg4.sh

echo "#!/bin/bash" > omg5.sh
echo "omg5"
find -maxdepth 2 -name "*.gz" >> omg5.sh
find -maxdepth 2 -name "*.zip" >> omg5.sh

echo "#!/bin/bash" > zomg.sh
echo "IJmuiden"
find -maxdepth 3 ! -name "*.*" >> zomg.sh
