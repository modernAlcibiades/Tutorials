solc-select use 0.8.7

certoraRun ReserveListFixed.sol:ReserveList --verify ReserveList:Reserve.spec \
--optimistic_loop \
--loop_iter 3 \
--send_only \
--msg "${1}"

# --optimistic_loop and --loop_iter 3 are flags that handle loops.
# They are needed here, but don't mind them, you will learn about loop handling in a future lesson.