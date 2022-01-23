def custom_range(index_cap, start_index=0, step=1):
    output = []
    while start_index != index_cap:
        output.append(start_index)
        start_index += step
    return output
