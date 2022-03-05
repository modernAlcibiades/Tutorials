methods {
		getCurrentManager(uint256 fundId) returns (address) envfree
		getPendingManager(uint256 fundId) returns (address) envfree
		activeManagerMap(address a) returns (bool) envfree
}

invariant ManagerZeroIsNotActive()
        !activeManagerMap(0)

rule uniqueManager(uint256 fundId1, uint256 fundId2, method f) {
	require fundId1 != fundId2;
    requireInvariant ManagerZeroIsNotActive();
    require getCurrentManager(fundId1) != 0 => activeManagerMap(getCurrentManager(fundId1));
	require getCurrentManager(fundId2) != 0 => activeManagerMap(getCurrentManager(fundId2));
	require getCurrentManager(fundId1) != getCurrentManager(fundId2) ;
				
	env e;
	// if (f.selector == claimManagement(uint256).selector)
	// {
	// 	uint256 id;
	// 	require id == fundId1 || id == fundId2;
	// 	claimManagement(e, id);  
	// } 
	// else {
		calldataarg args;
		f(e,args);
	// }
	assert getCurrentManager(fundId1) != getCurrentManager(fundId2), "managers not different";
	assert getCurrentManager(fundId1) != 0 => activeManagerMap(getCurrentManager(fundId1)), "manager of fund1 is not active";
	assert getCurrentManager(fundId2) != 0 => activeManagerMap(getCurrentManager(fundId2)), "manager of fund2 is not active";
}

ghost activeManagerMap(address) returns bool {
	init_state axiom forall address m. activeManagerMap(m) == false;
}

hook Sstore isActiveManager[KEY address a] bool value (bool old_value) STORAGE {
	havoc activeManagerMap assuming forall address m. m == a?
	activeManagerMap@new(a) == value:
	activeManagerMap@new(a) == activeManagerMap@old(a);
	//activeManagerMap[a] = value;
		// axiom forall m. 
		// m == a?
	 	// activeManagerMap@new[a] = value :
		// activeManagerMap@new[a] = activeManagerMap@old[a];
}

// invariant uniqueManagerInvariant(uint256 fundId1, uint256 fundId2)
// 	fundId1 ! = fundId2 => getCurrentManager(fundId1) != getCurrentManager(fundId2)
// 	{
// 		preserved {
// 			getCurrentManager(fundId1) != 0 => activeManagerMap[fundId1];
// 			getCurrentManager(fundId2) != 0 => activeManagerMap[fundId2];
// 		}
// 	}