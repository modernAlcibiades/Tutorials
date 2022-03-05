## Popsicle Finance properties

- Valid States (per user)
  ```
      Active : User balance > 0
      Inactive : User balance 0
  ```

- State Transitions
  - (low) `Inactive` : on `deposit() && msg.value > 0` => `Active`
  - (high)`Inactive` : on `withdraw(amount) && amount !=0` => Incorrect state, should revert
  - (low) `Inactive` : on `collectFees()` => No fees, 0 Rewards, state `Inactive`
  - (high) `Active` : on `deposit() && msg.value > 0` => `Active`
  - (high) `Active` : on `withdraw(amount) && amount < balances[msg.sender` => `Active`
  - (high) `Active` : on `withdraw(amount) && amount == balances[msg.sender` => `Inactive`
  - (high) `Active` : on `collectFees()` => update FeesCollectedPerShare, reset Rewards to 0, state `Active`

- Variable Transitions
  - (high) `totalFeesEarnedPerShare` increases monotonically
  - (medium) `Inactive` => Reward can only decrease (to 0)
  - (high) `feesCollectedPerShare` increases monotonically
  - (high) only accrue functions should increase reward

- High-level properties
  - (high) ERC20 properties should hold for balances
  - (high) There shouldn't be any fees/rewards while `Inactive`
  - (high) Cannot withdraw more than deposits
  - (high) Collected fees shouldn't be negative ie `totalFeesEarnedPerShare >= feesCollectedPerShare` for all users
  - (high) Only msg.sender action can change their balance
  
- Unit tests
  - (high) `totalFeesEarnedPerShare >= feesCollectedPerShare`
  - (high)`withdraw(amount) : amount <= balances[msg.sender]`  
