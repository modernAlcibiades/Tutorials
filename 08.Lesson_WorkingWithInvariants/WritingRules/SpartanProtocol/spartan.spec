using IERC20 as erc20

methods {
    init_pool()
    add_liquidity() returns uint256
    remove_liquidity(uint LP_tokens)
    swap(address from_token)
    getContractAddress() returns address envfree
    getToken0DepositAddress() returns address envfree
    getToken1DepositAddress() returns address envfree
    sync() envfree
    balanceOf(address) returns uint256 envfree
    allowance(address, address) returns uint256 envfree
}

// Ghost variables that follow private variables
// K
ghost kValue() returns uint256 {
    init_state axiom kValue() == 0;
}
hook Sstore K uint256 value (uint256 old_value) STORAGE {
    havoc kValue assuming kValue@new() == value;
}

// total
ghost totalValue() returns uint256 {
    init_state axiom totalValue() == 0;
}
hook Sstore total uint256 value (uint256 old_value) STORAGE {
    havoc totalValue assuming totalValue@new() == value;
}


// @note : need to replace t0 and t1 with ERC20 balance of the contract
// token0
ghost t0() returns uint256 {
    init_state axiom t0() == 0;
}
hook Sstore token0Amount uint256 value (uint256 old_value) STORAGE {
    havoc t0 assuming t0@new() == value;
}

// token1
ghost t1() returns uint256 {
    init_state axiom t1() == 0;
}
hook Sstore token1Amount uint256 value (uint256 old_value) STORAGE {
    havoc t1 assuming t1@new() == value;
}

// Vacuity check
rule vacuous(method f){
    env e; calldataarg args;
    f(e, args);
    assert (false);
}

invariant nonZeroTokenRatio()
    t0()>0 <=> t1()>0
    {
        preserved with(env e){
            sync();
        }
    }

invariant nonZeroTotal()
    totalValue() >0 <=> t0()*t1() > 0
    {
        preserved with(env e){
            sync();
        }
    }

// //Only init_pool & addLiquidity should change the following ratio
// rule kValueChanged(method f){
//     sync();
//     require(totalValue() > 0);
//     uint256 before = (t1()*t0())/(totalValue()*totalValue());
//     env e; calldataarg args;
//     f(e, args);
//     sync();
//     uint256 after = (t1()*t0())/(totalValue()*totalValue());
//     assert(before == after);
// }

rule t0t1RatioChanged(method f){
    require(t0()>0);
    uint256 before = (t1()/t0());
    env e; calldataarg args;
    f(e, args);
    uint256 after = (t1()/t0());
    assert(before == after);
}

rule swapCycleIncreases_token0Amount(){
    env e;
    uint256 before = t0();
    swap(e, getToken0DepositAddress());
    swap(e, getToken1DepositAddress());
    uint256 after = t0();
    assert (before <= after);
}

rule swapCycleIncreases_token1Amount(){
    env e;
    uint256 before = t1();
    swap(e, getToken0DepositAddress());
    swap(e, getToken1DepositAddress());
    uint256 after = t1();
    assert (before <= after);
}

// User should be able to withdraw all liquidity
rule withdrawAllLiquidityCorrect(){
    env e;
    uint256 balance = balanceOf(e.msg.sender);
    sync();
    require(totalValue() > 0);
    uint256 previous_t0 = t0();
    //uint256 previous_t1 = t1();
    remove_liquidity(e, balance);
    uint256 new_balance = balanceOf(e.msg.sender);
    sync();
    assert(new_balance == 0 && (t0()/previous_t0 == totalValue() + balance/ totalValue()), "Token0 balance incorrect");
    //assert(previous_t1/(t0() + previous_t1) == balance/ totalValue(), "Token1 balance incorrect");
}

// Protocol didn't lose funds to external users
// Should only fail for reduce
rule noReductionInFunds(method f){
    env e;
    require(currentContract != e.msg.sender);
    require(allowance(currentContract, e.msg.sender) == 0);
    require(totalValue() > 0);
    sync();
    uint256 before0 = t0();
    ///uint256 before1 = t1();
    calldataarg args;
    f(e, args);
    sync();
    uint256 after0 = t0();
    //uint256 after1 = t1();
    assert(before0 == after0);
    //assert(before1 == after1);
}

// Token ratios only change on swap, transfer, or add_liquidity
rule userTakesProportionalAmount(method f){
    env e;
    require(currentContract != e.msg.sender);
    require(allowance(currentContract, e.msg.sender) == 0);
    require(totalValue() > 0);
    sync();
    uint256 before0 = t0();
    uint256 before1 = t1();
    require(before1 > 0);
    calldataarg args;
    f(e, args);
    sync();
    uint256 after0 = t0();
    uint256 after1 = t1();
    assert((after0 ==0 && after1 == 0) ||(before0/before1 == after0/after1));
}