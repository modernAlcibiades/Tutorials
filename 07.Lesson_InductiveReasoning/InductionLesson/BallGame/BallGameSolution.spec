
methods {
	ballAt() returns uint256 envfree
}

invariant neverReachPlayer4() 
	// @note : Modified invariant to a stronger precondition
	// @note : The preserve will hold for ballAt = 3 in solidity contract since precondition itself is false
	// is p(n)=>p(n+1) iteratively, but p(0) is False, hence (p(0)=>p(1)) is True, 
	ballAt() != 3 && ballAt() != 4 