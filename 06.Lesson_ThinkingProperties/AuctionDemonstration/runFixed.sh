  solc-select use 0.5.12
 
 certoraRun AuctionFixed.sol:System \
    --verify System:Auction.spec \
    --msg "06 Auction -Run Fixed" \
    --send_only
