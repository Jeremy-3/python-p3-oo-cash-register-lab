#!/usr/bin/env python3

class CashRegister:
  def __init__(self, discount=0):
      self.discount = discount
      self.total = 0
      self.items = []
      self.last_item = None
      
  pass
  def add_item(self, title, price,quantity=1):
    self.total +=price * quantity
   
    self.items.extend([title] * quantity)
    
    self.last_item = (title, price, quantity) 
  
  def apply_discount(self):
    if self.discount > 0:
      discount_amount = (self.discount / 100) * self.total
      self.total -= discount_amount
      print(f"After the discount, the total comes to ${self.total:.0f}.")
    
    else:
      print("There is no discount to apply.")
    return self.items
  
  def void_last_transaction(self):
    if self.last_item:
        title, price, quantity = self.last_item
        self.total -= price * quantity
        self.items.pop()  
        self.last_item = None  
    else:
        return "No transaction to void."