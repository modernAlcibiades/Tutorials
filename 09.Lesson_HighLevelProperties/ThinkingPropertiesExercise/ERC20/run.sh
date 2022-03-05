solc-select use 0.8.0

certoraRun ERC20Fixed.sol:ERC20 \
--verify ERC20:erc20.spec \
--send_only \
--msg "$1"