methods {
	getCurrentManager(uint256 fundId) returns (address) envfree
	getPendingManager(uint256 fundId) returns (address) envfree
	isActiveManager(address a) returns (bool) envfree
}

rule uniqueManagerAsRule(uint256 fundId1, uint256 fundId2, method f) {
	// assume different IDs
	require fundId1 != fundId2;
	// assume different managers
	require getCurrentManager(fundId1) != getCurrentManager(fundId2);
	
	require isActiveManager(getCurrentManager(fundId1));
	require isActiveManager(getCurrentManager(fundId2));
	// hint: add additional variables just to look at the current state
	// bool active1 = isActiveManager(getCurrentManager(fundId1));			
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

	address post1 = getCurrentManager(fundId1);
	address post2 = getCurrentManager(fundId2);
	// verify that the managers are still different 
	assert isActiveManager(post1), "Fund1 manager marked inactive";	
	assert isActiveManager(post2), "Fund2 manager marked inactive";	
	assert post1 != post2, "managers not different";
}


// rule managerIsActive(uint256 fundId, method f) {
// 	require isActiveManager(getCurrentManager(fundId));

// 	env e;
// 	calldataarg args;
// 	f(e,args);

// 	assert isActiveManager(getCurrentManager(fundId)), "Fund manager marked inactive";	
// }

// @note : Created a relevant invariant but addresss(0) causes syntax error
// invariant fundManagerIsActive(uint256 fundId)
// 	getCurrentManager(fundId) != 0 => isActiveManager(getCurrentManager(fundId))


// /* A version of uniqueManagerAsRule as an invariant */
// invariant uniqueManagerAsInvariant(uint256 fundId1, uint256 fundId2)
// 	(fundId1 != fundId2) && isActive(getCurrentManager(fundId1)) && isActive(getCurrentManager(fundId2)) => getCurrentManager(fundId1) != getCurrentManager(fundId2) 
