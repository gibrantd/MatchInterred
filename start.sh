
start=$(date +%s)

./process/splitter.sh
./process/producer.sh
./process/consumerDb.sh
./process/concilia.sh

end=$(date +%s)
runtime=$(python -c "print '%u:%02u' % ((${end} - ${start})/60, (${end} - ${start})%60)")

echo "$runtime"