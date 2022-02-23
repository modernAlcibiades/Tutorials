solc-select use $1

certoraRun BordaBug3.sol:Borda --verify Borda:Borda.spec \
--send_only \
--msg "$2"
