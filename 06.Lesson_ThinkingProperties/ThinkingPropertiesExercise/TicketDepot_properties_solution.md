## TicketDepot properties

- Valid States
    ```
    Uninitialized   : Event not created yet
    Ready           : Event created, sale started
    ResaleOnly      : Primary Sale finished, buy/sell offers available
    ```
- State Transitions
  - `Uninitialized` : on `createEvent(args)` => `Ready`
  - `Ready`: on `ticketsRemaining <= 0` =>  `ResaleOnly`
  
- Variable Transitions
  - `ticketsRemaining` decreases monotonically
  - address(this).balance increases monotonically
  
- High-level properties
  - Each event should have unique id
  - Tickets for uncreated events cannot be sold or offered
  - Balance of the contract should never decrease
  - Only offered tickets can be bought
  - One ticket can only have one attendee
  - Seller can only be the attendee
  
- Unit tests
  - `ticketsRemaining` < `_ticketsAvailable`