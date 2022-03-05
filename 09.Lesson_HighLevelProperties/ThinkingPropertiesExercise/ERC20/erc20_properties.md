## ERC20 Properties

- Valid States
  - Address balance states
    - NoUser : No token balance
    - User : Has balance > 0
  - Allowance states
    - NoSpender_a : Has allowance == 0 for address a
    - Spender_a : Has allowance > 0 for address a

- State Transitions
  - (high)`NoUser`  : on receiving funds => `User` 
  - (high)`User` : on sending out whole balance => `NoUser`
  - (high)`NoSpender_a` : on being approved by address a => `Spender_a`
  - (high)`Spender_a` : on spending allowance => `NoSpender_a`
  - (high)`Spender_a` : address `a` cancels allowance => `NoSpender_a`
  
- Variable Transitions
  - (low) Name and symbol should not change once set
  - (medium) Decimals should not change once set

- High-level Properties
  - (high) Only user and anyone approved by user should be able to withdraw funds from user's account
  - (medium) User should be able to revoke allowance
  - (high) User can only transfer amount less than their balance
  - (high) Sender balance + Recipient balance should stay fixed across operations
  - (low) Approval for spending should have time limits
  
- Unit Tests
  - (high) For all addresses a, `_totalSupply >= _balances[a]`