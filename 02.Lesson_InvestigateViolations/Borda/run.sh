solc-select use $1

certoraRun BordaBug1.sol:Borda --verify Borda:Borda.spec \
--send_only \
--msg "$2"
