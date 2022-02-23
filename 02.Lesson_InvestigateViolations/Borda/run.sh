solc-select use 0.7.6

for N in 1 2 3 4
do
echo BordaBug${N}.sol
certoraRun BordaBug${N}.sol:Borda \
--verify Borda:Borda.spec \
--send_only \
--msg "BordaBug${N}_fixed"
done
