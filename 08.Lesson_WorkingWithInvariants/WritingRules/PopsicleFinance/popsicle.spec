// ghost userShare(address) returns uint256  {
//     init_state axiom forall address user. userShare(user) = 0
// }

// hook Sstore totalFeesEarnedPerShare uint256 value 
//     (uint256 old_value) STORAGE {
//         havoc forall address user. userShare@new(user) = 
//     }


methods {
    assetsOf(address) envfree
}

// Assets of a user should not change except defined functions

function userAssetsChangeFunctions(method f) returns bool{
    return (
        f.selector == OwnerDoItsJobAndEarnsFeesToItsClients().selector ||
        f.selector == collectFees().selector 
    );
}

rule userAssetsNotChanged(address user, method f){
    uint256 assetsBefore = assetsOf(user);
    env e;
    calldataarg args;
    f(e, args);
    uint256 assetsAfter = assetsOf(user);
    assert (userAssetsChangeFunctions(f) || assetsBefore == assetsAfter, "Assets changed upexpetedly");
}