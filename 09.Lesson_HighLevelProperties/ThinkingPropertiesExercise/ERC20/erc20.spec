
// some properties based on bank example in 07
methods {
    totalSupply() returns uint256 envfree
    balanceOf(address) returns uint256 envfree
    allowance(address, address) returns uint256 envfree
    decimals() returns uint8 envfree
    transferFrom(address, address, uint256)
}

ghost og_decimals() returns uint8{
    init_state axiom og_decimals() == decimals(); 
}

ghost sum_of_all_funds() returns uint256{
    // for the constructor - assuming that on the constructor the value of the ghost is 0
    init_state axiom sum_of_all_funds() == 0;
}

hook Sstore _balances[KEY address user] uint256 new_balance
    // the old value ↓ already there
    (uint256 old_balance) STORAGE {
  havoc sum_of_all_funds assuming sum_of_all_funds@new() == sum_of_all_funds@old() + new_balance - old_balance;
}

invariant totalSupply_GE_singleUserBalance()
    forall address user. sum_of_all_funds() >= balanceOf(user)

invariant totalSupply_Equals_sumOfUserBalances()
    totalSupply() == sum_of_all_funds()

invariant metadataConstant()
    decimals() == og_decimals()

rule balanceOfThirdPartyNotChanged(address sender, address receiver, address third_party, uint256 amount){
    env e;
    require(sender != third_party && receiver != third_party);
    uint256 balanceBefore = balanceOf(third_party);
    transferFrom(e, sender, receiver, amount);
    assert( balanceOf(third_party) == balanceBefore);
}

rule allowanceNotChanged(address spender, address third_party, address random, uint256 amount, method f){
    env e;
    require(third_party != e.msg.sender);
    require (
        f.selector == approve(address, uint256).selector ||
        f.selector == decreaseAllowance(address, uint256).selector ||
        f.selector == increaseAllowance(address, uint256).selector ||
        f.selector == transfer(address, uint256).selector
    );
    uint256 allowanceBefore = allowance(third_party, random);
    f(e, spender, amount);
    assert(allowance(third_party, random) == allowanceBefore);
}




