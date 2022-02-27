methods {

    totalSupply() returns uint256 envfree

    balanceOf(address) returns uint256 envfree

    transfer(address, uint256) returns bool 

    allowance(address, address) returns uint256 envfree

    approve(address, uint256) returns bool

    transferFrom(address, address, uint256) returns bool

    name() returns string envfree

    symbol() returns string envfree

    decimals() returns uint8 envfree
}