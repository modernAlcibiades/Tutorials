methods {
    getTokenAtIndex(uint256) returns address envfree
    getIdOfToken(address) returns uint256 envfree
    getReserveCount() returns uint256 envfree
    addReserve(address, address, address, uint256) envfree
    removeReserve(address) envfree
}

rule checkVacuous(method f){
    env e;
    calldataarg args;
    f(e, args);
    assert(false);
}

// Either correlated 
invariant listsCorrelated(uint256 id)
    getIdOfToken(getTokenAtIndex(id)) == id
    {
        preserved {
            require(getTokenAtIndex(id) != 0);
        }
    }
    
// Invariant to make sure number of
invariant noTokenAtGreaterThanReserveCount (uint256 id)
    id >= getReserveCount() => getTokenAtIndex(id) == 0

invariant injectiveIds (address token1, address token2)
    token1 != token2 => getIdOfToken(token1) != getIdOfToken(token2)
    

