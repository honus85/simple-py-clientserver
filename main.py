from order import Order
from publisher import Publisher
import server_admin
import datetime


def generate_random_orders(num):
    order_prefix = 1234567800
    orders = []
    for i in range(num):
        cl_order_id = "Order" + str(order_prefix + i)
        symbol = "0005.HK"
        side = "Buy"
        transact_time = str(datetime.datetime.now())
        ord_type = "Limit"
        text = "New Order Single"
        price = 66
        order_single = Order(cl_order_id, symbol, side, transact_time, ord_type, text, price)
        orders.append(order_single)
    return orders


if __name__ == "__main__":
    server_admin.start_server()
    host = server_admin.host
    port = server_admin.port
    orders_to_send = generate_random_orders(10)
    publisher = Publisher(host, port)
    for order in orders_to_send:
        publisher.publish(order)
    publisher.close()
    server_admin.stop_server()
