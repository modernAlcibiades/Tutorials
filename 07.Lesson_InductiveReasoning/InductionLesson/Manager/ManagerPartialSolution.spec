methods {
		getCurrentManager(uint256 fundId) returns (address) envfree
		getPendingManager(uint256 fundId) returns (address) envfree
		isActiveManager(address a) returns (bool) envfree
}



rule uniqueManager(uint256 fundId1, uint256 fundId2, method f) {
	// @note : Do not need the initial addresses to be non-zero
	// Instead, we should check 0 addresses too in the pre-condition
	// since default value before fund creation is 0, and is a valid state
	require fundId1 != fundId2;
	require isActiveManager(getCurrentManager(fundId1));
	require isActiveManager(getCurrentManager(fundId2));
	require getCurrentManager(fundId1) != getCurrentManager(fundId2) ;
				
	env e;
	if (f.selector == claimManagement(uint256).selector)
	{
		uint256 id;
		require id == fundId1 || id == fundId2;
		claimManagement(e, id);  
	}
	else {
		calldataarg args;
		f(e,args);
	}
	// If pre-condition has 0 addresses, post-condition should also have 0 addresses
	assert getCurrentManager(fundId1) != getCurrentManager(fundId2), "managers not different";
	assert isActiveManager(getCurrentManager(fundId1)), "manager of fund1 is not active";
	assert isActiveManager(getCurrentManager(fundId2)), "manager of fund2 is not active";
}



		
	
