solc-select use 0.8.11

certoraRun Loops.sol:Loops --verify Loops:LoopsUnrolling.spec \
--send_only \
--optimistic_loop \
--loop_iter 10 \
--msg "$1"