solc-select use 0.8.0

certoraRun ERC20Bug2.sol:ERC20 --verify ERC20:ERC20.spec \
--optimistic_loop \
--send_only \
--msg "$1"