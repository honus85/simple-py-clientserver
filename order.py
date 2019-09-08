class Order:

    def __init__(self,
                 cl_order_id,
                 symbol,
                 side,
                 transact_time,
                 order_qty,
                 ord_type,
                 text,
                 price=0):
        self.cl_order_id = cl_order_id
        self.symbol = symbol
        self.side = side
        self.transact_time = transact_time
        self.order_qty = order_qty
        self.ord_type = ord_type
        self.text = text
        self.price = price

    def print_order_details(self):
        print("Order Details: " + self.cl_order_id \
              + " " + self.symbol \
              + " " + self.side \
              + " " + self.transact_time \
              + " " + self.order_qty \
              + " " + self.ord_type \
              + " " + self.text \
              + " " + self.price)
