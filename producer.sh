
archivos=$(ls /Users/interware/Documents/IW/PROSA/Match-Interredes/Lab/init/* | wc -l)
echo $archivos

while   [ ${archivos} -lt 20 ]; 
do 
 archivos=$(ls /Users/interware/Documents/IW/PROSA/Match-Interredes/Lab/init/* | wc -l)
 echo "esperando..."
done
sleep 1
python3 process/producer.py interredes0aa &
python3 process/producer.py interredes0ab &
python3 process/producer.py interredes0ac &
python3 process/producer.py interredes0ad &
python3 process/producer.py interredes0ae &
python3 process/producer.py interredes0af &
python3 process/producer.py interredes0ag &
python3 process/producer.py interredes0ah &
python3 process/producer.py interredes0ai &
python3 process/producer.py interredes0aj &
python3 process/producer.py interredes0ak &
python3 process/producer.py interredes0al &
python3 process/producer.py interredes0am &
python3 process/producer.py interredes0an &
python3 process/producer.py interredes0ao &
python3 process/producer.py interredes0ap &
python3 process/producer.py interredes0aq &
python3 process/producer.py interredes0ar &
python3 process/producer.py interredes0as &
python3 process/producer.py interredes0at &


if [ -f "/Users/interware/Documents/IW/PROSA/Match-Interredes/Lab/init/interredes0au" ]
then
   python3 process/producer.py interredes0au & 
fi