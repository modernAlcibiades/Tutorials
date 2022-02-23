solc-select use $1

certoraRun BordaBug2.sol:Borda --verify Borda:Borda.spec \
--send_only \
--msg "$2"
