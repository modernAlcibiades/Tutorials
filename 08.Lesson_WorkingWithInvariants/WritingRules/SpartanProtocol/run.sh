solc-select use 0.8.4

certoraRun SpartaProtocolPool.sol:SpartaProtocolPool \
--verify SpartaProtocolPool:spartan.spec \
--send_only \
--loop_iter 2 \
--msg "$1"