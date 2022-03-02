## TicketDepot properties

- Valid States
  - Ticket states
    ```
        Uninitialized   : Ticket not created yet
        NotForSale      : Issued to an attendee, not on offer
        OnOffer         : Available for purchase
    ```

  - Event states
    ```
        Uninitialized   : Event not created yet
        Ready           : Event created, sale started
        ResaleOnly      : Primary Sale finished, buy/sell offers available
    ```
- State Transitions
  - Ticket states (id : TicketId)
    - (high) `Uninitialized` : on `buyNewTicket(args)` => `NotForSale`
    - (low) `NotForSale` : on `offerTicket(args)` => `OnOffer`
    - (high) `OnOffer` : on `buyOfferedTicket(args)` => `NotForSale`
  - Event states (id : EventId)
    - (medium) `Uninitialized` : on `createEvent(args)` => `Ready`
    - (high) `Ready`: on `ticketsRemaining <= 0` =>  `ResaleOnly`
    
- Variable Transitions
  - (medium) `numEvents` increases monotonically
  - (high) `ticketsRemaining` decreases monotonically
  - (medium) address(this).balance increases monotonically
  
- High-level properties
  - (high) Each event should have unique id
  - (medium) Tickets for uncreated events cannot be sold or offered
  - (medium) Balance of the contract should never decrease
  - (medium) Only offered tickets can be bought
  - (high) One ticket can only have one attendee
  - (high) Seller can only be the attendee
  - (high) Offered tickets cannot be bought after deadline
  - (high) If specified, only Buyer should be able to buy an offered ticket
  
- Unit tests
  - (high) `ticketsRemaining` <= `_ticketsAvailable`