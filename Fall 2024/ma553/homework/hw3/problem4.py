def time_per_floating_point_operation(flops_per_second):
    return 1 / flops_per_second

# FLOPS (Floating Point Operations Per Second)
mega_flops = 10**6
giga_flops = 10**9
tera_flops = 10**12
peta_flops = 10**15
exa_flops = 10**18

# Time per floating point operation in seconds
time_mega = time_per_floating_point_operation(mega_flops)
time_giga = time_per_floating_point_operation(giga_flops)
time_tera = time_per_floating_point_operation(tera_flops)
time_peta = time_per_floating_point_operation(peta_flops)
time_exa = time_per_floating_point_operation(exa_flops)

print(f"Time per floating point operation at 1 megaflop per second: {time_mega} seconds")
print(f"Time per floating point operation at 1 gigaflop per second: {time_giga} seconds")
print(f"Time per floating point operation at 1 teraflop per second: {time_tera} seconds")
print(f"Time per floating point operation at 1 petaflop per second: {time_peta} seconds")
print(f"Time per floating point operation at 1 petaflop per second: {time_exa} seconds")
