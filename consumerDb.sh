archivos=$(ls /Users/interware/Documents/IW/PROSA/Match-Interredes/Lab/key/* | wc -l)
echo $archivos

while   [ ${archivos} -lt 20 ]; 
do 
 archivos=$(ls /Users/interware/Documents/IW/PROSA/Match-Interredes/Lab/key/* | wc -l)
 echo "esperando...$archivos"
done

sleep 2
python3 process/consumerDb.py interredes0aa.txt &
python3 process/consumerDb.py interredes0ab.txt &
python3 process/consumerDb.py interredes0ac.txt &
python3 process/consumerDb.py interredes0ad.txt &
python3 process/consumerDb.py interredes0ae.txt &
python3 process/consumerDb.py interredes0af.txt &
python3 process/consumerDb.py interredes0ag.txt &
python3 process/consumerDb.py interredes0ah.txt &
python3 process/consumerDb.py interredes0ai.txt &
python3 process/consumerDb.py interredes0aj.txt &
python3 process/consumerDb.py interredes0ak.txt &
python3 process/consumerDb.py interredes0al.txt &
python3 process/consumerDb.py interredes0am.txt &
python3 process/consumerDb.py interredes0an.txt &
python3 process/consumerDb.py interredes0ao.txt &
python3 process/consumerDb.py interredes0ap.txt &
python3 process/consumerDb.py interredes0aq.txt &
python3 process/consumerDb.py interredes0ar.txt &
python3 process/consumerDb.py interredes0as.txt &
python3 process/consumerDb.py interredes0at.txt &


if [ -f "/Users/interware/Documents/IW/PROSA/Match-Interredes/Lab/key/interredes0au.txt " ]
then
   python3 process/consumerDb.py interredes0au.txt &
fi
