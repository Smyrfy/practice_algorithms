def merge_orders(web_orders: list, app_orders: list) -> list:
    merged = []

    i = 0
    j = 0

    while i < len(web_orders) and j < len(app_orders):

        if web_orders[i] < app_orders[j]:
            merged.append(web_orders[i])
            i += 1
        else:
            merged.append(app_orders[j])
            j += 1

    while i < len(web_orders):
        merged.append(web_orders[i])
        i += 1

    while j < len(app_orders):
        merged.append(app_orders[j])
        j += 1

    return merged