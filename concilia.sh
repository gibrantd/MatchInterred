
archivos=$(cat done/trxOk.txt | wc -l)
echo $archivos

while   [ ${archivos} -lt 2000000 ]; 
do 
 archivos=$(cat done/trxOk.txt | wc -l)
 echo "esperando..."
done


echo $(date)
echo "Coinciliando..."

sleep 3

cat   key/interredes0aa.txt >> done/trxTotal.txt 
cat   key/interredes0ab.txt >> done/trxTotal.txt 
cat   key/interredes0ac.txt >> done/trxTotal.txt 
cat   key/interredes0ad.txt >> done/trxTotal.txt 
cat   key/interredes0ae.txt >> done/trxTotal.txt 
cat   key/interredes0af.txt >> done/trxTotal.txt 
cat   key/interredes0ag.txt >> done/trxTotal.txt 
cat   key/interredes0ah.txt >> done/trxTotal.txt 
cat   key/interredes0ai.txt >> done/trxTotal.txt 
cat   key/interredes0aj.txt >> done/trxTotal.txt 
cat   key/interredes0ak.txt >> done/trxTotal.txt 
cat   key/interredes0al.txt >> done/trxTotal.txt 
cat   key/interredes0am.txt >> done/trxTotal.txt 
cat   key/interredes0an.txt >> done/trxTotal.txt 
cat   key/interredes0ao.txt >> done/trxTotal.txt 
cat   key/interredes0ap.txt >> done/trxTotal.txt 
cat   key/interredes0aq.txt >> done/trxTotal.txt 
cat   key/interredes0ar.txt >> done/trxTotal.txt 
cat   key/interredes0as.txt >> done/trxTotal.txt 
cat   key/interredes0at.txt >> done/trxTotal.txt 

if [ -f "key/interredes0au.txt" ]
then
   cat   key/interredes0au.txt >> done/trxTotal.txt 
fi



sdiff <(sort /Users/interware/Documents/IW/PROSA/Match-Interredes/Lab/done/trxOk.txt) <(sort /Users/interware/Documents/IW/PROSA/Match-Interredes/Lab/done/trxTotal.txt)  | grep ">" | awk -F">" '{print $2}' | awk -F"\t" '{print $2}' > /Users/interware/Documents/IW/PROSA/Match-Interredes/Lab/done/trxErr.txt

rm -rf /Users/interware/Documents/IW/PROSA/Match-Interredes/Lab/done/trxTotal.txt

cat /Users/interware/Documents/IW/PROSA/Match-Interredes/Lab/done/trxErr.txt

echo "Finalizando Conciliación..."
echo $(date)