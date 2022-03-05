## Spartan properties

- Valid States
  - Pool
  ```
    Uninitialized : Pool doesn't exist
    PoolActive : Pool is functional and can be used
    PoolPaused : Pool is not active and cannot be used
  ```
  - User
  ```
    NonProvider : No share of liquidity in the pool
    Liquidity Provider : Amount of liquidity in the pool > 0
  ```

- State Transitions
  - `Uninitialized` : on `init_pool` => `PoolActive`
  - `NonProvider` : on `add_liquidity` => `Liquidity Provider`
  - `Liquidity Provider` : on `add_liquidity` => `Liquidity Provider`
  - `Liquidity Provider` : on `remove_liquidity` for all liquidity provided => `NonProvider`
  - Other functions maintain the states
  
- Variable Transitions
  - `token0Amount` == 0 if `Uninitialized`, >0 otherwise
  - `token1Amount` == 0 if `Uninitialized`, >0 otherwise
  - `total_supply >0` <=> `token0amount > 0` <=> `token1amount > 0`
  - `total_supply ==0` <=> `token0amount == 0` <=> `token1amount == 0`

- High-level properties
  - (high) The token balances in the pool
  - (high) Each swap increases the balance of one token and reduces the balance of other
  - (medium) for a pool of tokens (t1, t2) `swap(t1)`, followed by reverse action `swap(t2)` should increase the balance of both tokens in the pool
  - (high) Liquidity Provider should always be able to withdraw their liquidity
  - (high) If the totalSupply is not zero, then there must be both types of tokens in the pool
  - (high) If user added liquidity in the pool, they should be able to remove proportional amount of liquidity
  
- Unit Tests
  - 

  